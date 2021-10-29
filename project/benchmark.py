"""
Benchmarking class for RocksDB.
"""
import subprocess
import sys
import re
import pdb
import project.rocksdb_config as rocksconfig
import project.neo4j_config as neoconfig
import numpy as np


class RocksdbBenchmark:
    def __init__(self, bench_type=None, options={}):
        """
        RocksDB benchmark class.

        bench_type -> The following benchmark types are supported:
            'mix' -> 'migraph' with 78% GET, 13% PUT, 6% DELETE, 3% Iterate.
            'random' -> 'readrandom' with only read operations of keys in random order.
            'ycsb' ->  Run a YCSB benchmark. Default workload is A unless specified by in the options argument.

        options -> Additional options can be provided:
            {
            'threads': number of threads -> Run benchmarck using a multiple threads (default is 1).
            'output_file': desired file path -> append throughput test results to a file. If file doesn't exist, it will be created.
            'ycsb_workload': workload type -> workload type: one of: <a,b,c,d,e,f>.
            'baseline': throughput value -> value to use as a baseline for testing comparisons.
            'testing': True or False -> calculate averages and deviations from baseline during testing.
            'readwritepercent': percentage [default: 90] -> Ratio of reads to reads/writes for the ReadRandomWriteRandom workload
            }
        """
        self.knobs = {}
        self.benchmarks = []
        self.ycsb = False
        self.__ycsb_workload = "a"
        self.__threads = 1
        self.__output_file = ""
        self.__testing = False
        self.baseline = 0
        self.__readwritepercent = None

        # One can input multiple commands in one list if that is desired.
        if bench_type.lower() == "mix":
            self.benchmarks = ["mixgraph"]
        elif bench_type.lower() == "ycsb":
            self.ycsb = True
            if "ycsb_workload" in options:
                self.__ycsb_workload = options["ycsb_workload"].lower()
        else:
            self.benchmarks = [bench_type.lower()]

        if "threads" in options:
            self.__threads = str(options["threads"])
        if "output_file" in options:
            self.__output_file = options["output_file"]
        if "testing" in options:
            self.__testing = options["testing"]
        if "baseline" in options:
            self.baseline = int(options["baseline"])
        if "readwritepercent" in options:
            self.__readwritepercent = int(options["readwritepercent"])

    def change_threads(self, threads):
        self.__threads = threads

    def load_knob_configurations(self, knobs):
        """
        Adds the knob configurations for a benchmark run
        Each knob has a valid name as the key and value

        Arguments:
            knobs -> key-value pairs of knobs to tune
        """
        self.knobs = knobs
        if self.__testing and len(self.__output_file) > 0:
            with open(self.__output_file, "a") as file:
                file.write("\n\nBenchmark with knobs: " + str(self.knobs) + "  ")

    def add_command_options(self, options_file=False):
        """
        Add knob configuration to the command, eitheror CLI flags or an optionsfile

        Arguments:
            options_file -> Use an options-file (True) with a pre-defined path in config.py or use command line flags (False)
        """
        result = ""
        if options_file or self.ycsb:
            file_path = (
                rocksconfig.YCSB_OPTIONS_FILE if self.ycsb else rocksconfig.OPTIONS_FILE
            )
            template_path = (
                rocksconfig.YCSB_OPTIONS_FILE_TEMPLATE
                if self.ycsb
                else rocksconfig.OPTIONS_FILE_TEMPLATE
            )
            # Read options_file parameters and find alter coresponding knobs.
            with open(template_path, "r") as file:
                data = file.readlines()
                for i, line in enumerate(data):
                    if "=" in line.strip():
                        kv_pair = line.strip()
                        key, value = kv_pair.split("=", 1)
                        if key in self.knobs:
                            data[i] = "  " + key + "=" + self.knobs[key] + "\n"

            # Finally, write the new data
            with open(file_path, "w") as file:
                file.writelines(data)

            # Add options file to command
            if self.ycsb:
                result += f" -p rocksdb.optionsfile={file_path}"
            else:
                result += f" options_file={file_path}"

        else:  # We provide command line flags instead.
            single_dashed = ["compression"]
            if len(self.knobs.keys()) > 0:
                for knob in self.knobs:
                    if knob in single_dashed:
                        result += f" -{knob}={self.knobs[knob]}"
                    else:
                        result += f" --{knob}={self.knobs[knob]}"

        return result

    def run_filling(self, fill_type="random", num_million=1, options_file=False):
        """
        Create and fill a database instance with key-value pairs

        Arguments:
            fill_type -> random (default) or seq (sequential)
            num_million -> number of million key-value pairs to fill
        """
        if self.ycsb:
            command = f"sudo {rocksconfig.YCSB_PATH}bin/ycsb.sh load rocksdb -s -P {rocksconfig.YCSB_PATH}workloads/workload{self.__ycsb_workload} -P {rocksconfig.YCSB_PROPERTIES_FILE} -p rocksdb.dir={rocksconfig.DB_DIR_YCSB}"
        else:
            if "mixgraph" in self.benchmarks:
                command = f'sudo {rocksconfig.BENCHMARK_COMMAND_PATH} --benchmarks="fill{fill_type}" -num={num_million*1000000} -perf_level=3 -use_direct_io_for_flush_and_compaction=true -use_direct_reads=true -cache_size=268435456 -key_size=48 -value_size=43'
            else:
                command = f'sudo {rocksconfig.BENCHMARK_COMMAND_PATH} --benchmarks="fill{fill_type}" -num={num_million*1000000}'

        # print(command)
        try:
            # subprocess.run(f'sudo rm -r {rocksconfig.DB_DIR}/', shell=True)
            subprocess.run(command, shell=True)
        except subprocess.CalledProcessError:
            print(
                "Error running the filling benchmark, please check the command format and paths given."
            )
            sys.exit()

    def run_benchmark(
        self,
        runs=1,
        num_million=1,
        fill=False,
        options_file=False,
        max_seconds=30,
        use_existing=False,
        calc_latency=False,
    ):
        """
        Run a benchmark and parse the throughput results.
        """
        benchmarks = f'"{",".join(self.benchmarks)}"'
        if self.ycsb:
            command = f"sudo {rocksconfig.YCSB_PATH}bin/ycsb.sh run rocksdb -s -P {rocksconfig.YCSB_PATH}workloads/workload{self.__ycsb_workload} -P {rocksconfig.YCSB_PROPERTIES_FILE} -p rocksdb.dir={rocksconfig.DB_DIR_YCSB} -threads 32"
        else:
            # command = f'sudo {rocksconfig.BENCHMARK_COMMAND_PATH} -db={rocksconfig.DB_DIR} --benchmarks={benchmarks}'
            command = (
                f"sudo {rocksconfig.BENCHMARK_COMMAND_PATH} --benchmarks={benchmarks}"
            )
            if use_existing:
                command += " --use_existing_db"
            if "mixgraph" in benchmarks:
                command += (
                    " -use_direct_io_for_flush_and_compaction=true -use_direct_reads=true "
                    "-cache_size=268435456 -keyrange_dist_a=14.18 -keyrange_dist_b=-2.917 "
                    "-keyrange_dist_c=0.0164 -keyrange_dist_d=-0.08082 -keyrange_num=30 "
                    "-value_k=0.2615 -value_sigma=25.45 -iter_k=2.517 -iter_sigma=14.236 "
                    "-mix_get_ratio=0.85 -mix_put_ratio=0.14 -mix_seek_ratio=0.01 "
                    "-sine_mix_rate_interval_milliseconds=5000 -sine_a=1000 "
                    "-sine_b=0.000000073 -sine_d=4500000 --perf_level=1 -reads=4200000 "
                    f"-num={num_million*1000000} -key_size=48 --statistics=1"
                )
                # ' --allow_concurrent_memtable_write=false') # this last was added for multi-threading.
            else:
                command += f" -num={num_million*1000000}"

            command += f" --duration={max_seconds}"

        command += self.add_command_options(options_file)
        if "mixgraph" not in benchmarks:
            command += f" --threads={self.__threads}"
        if "readrandomwriterandom" in benchmarks:
            command += f" -readwritepercent={self.__readwritepercent}"
        print(command)

        try:
            # Save to later calculate average
            results = {
                "throughput": [],
                "latency": [],
            }
            # throughput, latency = -1, -1
            for _ in range(runs):
                if self.ycsb:
                    try:
                        subprocess.run(f"sudo rm -r {rocksconfig.DB_DIR_YCSB}")
                    except FileNotFoundError:
                        pass
                    self.run_filling(fill_type="random")
                else:
                    if fill:
                        self.run_filling(
                            fill_type="random",
                            num_million=num_million,
                            options_file=options_file,
                        )

                for line in subprocess.check_output(
                    command, shell=True, universal_newlines=True
                ).split("\n"):
                    if self.ycsb:
                        if "OVERALL" in str(line):
                            match = re.search("\d+[.]\d+", str(line))
                            if match is not None:
                                throughput = match.group(0)
                                results.append(float(throughput))
                    else:
                        # Find TPS and latency
                        if "ops/sec;" in str(line):
                            match = re.search("((\d+)\sops)", str(line))
                            throughput = match.group(2)
                            results["throughput"].append(int(throughput))

                            match = re.search("(([.\d]+)\smicros)", str(line))
                            latency = match.group(2)
                            results["latency"].append(float(latency))

            average_tps = int(sum(results["throughput"]) / len(results["throughput"]))
            if calc_latency:
                average_l = float(sum(results["latency"]) / len(results["latency"]))

            if len(self.__output_file) > 0:
                with open(self.__output_file, "a") as file:
                    if calc_latency:
                        file.write(f"\n{average_tps},{average_l}  ")
                    else:
                        file.write(f"\n{average_tps}  ")

        except subprocess.CalledProcessError:
            print(
                "Error running the benchmark, please check the command format and paths given."
            )
            sys.exit()

        # Finally, return the throughput
        if calc_latency:
            return average_tps, average_l
        else:
            return average_tps, -1


class Neo4jBenchmark:
    def load_knob_configurations(self, knobs):
        # Write to configuration file
        with open(neoconfig.TEMPLATE_FILE, "r") as template:
            with open(neoconfig.CONFIGURATION_FILE, "w") as file:

                for key, value in knobs.items():
                    file.write(f"{key}={value}\n")

                for line in template:
                    file.write(line)

        # temporary write configurations
        with open(neoconfig.CYPHER_DIR + "results.txt", "a") as file:
            for key, value in knobs.items():
                file.write(f"{key}={value}\n")


    def run_benchmark(self, runs=1):
        # Run benchmark command and parse output, return thoughput.
        throughput = []
        # command = (
        #     f". {neoconfig.CYPHER_DIR}scripts/environment-variables-default.sh; "
        #     + f"{neoconfig.CYPHER_DIR}scripts/load-in-one-step.sh; "
        #     + f"{neoconfig.CYPHER_DIR}driver/benchmark.sh"
        # )
        for _ in range(runs):
            # command = (
            #     f". {neoconfig.CYPHER_DIR}scripts/environment-variables-default.sh; "
            #     + f"{neoconfig.CYPHER_DIR}scripts/snapshot-load.sh; "
            #     + f"{neoconfig.CYPHER_DIR}driver/benchmark.sh; "
            #     + f"{neoconfig.CYPHER_DIR}python3 parse.py; "
            # )
            command = f" bash {neoconfig.CYPHER_DIR}program.sh; "
            try:
                for line in subprocess.check_output(
                    command, shell=True, universal_newlines=True, executable="/bin/bash", timeout=3000
                ).split("\n"):
                    print(line)
                    # NOTE: better method is to grab the results from the benchmark results JSON file
                    # if "op/s" in str(line):
                    #     match = re.search("(([\d.]+)\s[(])", str(line))
                    #     throughput = float(match.group(2))
            except subprocess.SubprocessError:
                pass

        # return np.mean(throughput)
        return 0
