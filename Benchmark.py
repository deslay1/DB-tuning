"""
Benchmarking class for RocksDB.
"""
import subprocess
import re
import config

class RocksdbBenchmark:
    def __init__(self, bench_type=None, options={}):
        """
        RocksDB benchmark class.

        bench_type -> The following benchmark types are supported:
            'mix' -> 'migraph' with 78% GET, 13% PUT, 6% DELETE, 3% Iterate.
            'random' -> 'readrandom' with only read operations of keys in random order.
            'ycsb' ->  Run a YCSB benchmark. Default workload is A unless specified by in the options argument.
        
        options -> Additional options can be provided:
            '{output_file: desired_file_path}' -> append throughput test results to a file. If file doesn't exist, it will be created.
            '{ycsb_workload: workload_type}' -> workload_type: one of: <a,b,c,d,e,f>.
            '{baseline: throughput_value}' -> value to use as a baseline for testing comparisons.
            '{testing: True or False}' -> calculate averages and deviations from baseline during testing.

        """
        self.knobs = {}
        self.benchmarks=[]
        self.__ycsb = False
        self.__ycsb_workload = 'a'
        self.__output_file = ''
        self.__testing = False
        self.__baseline = 0

        # One can input multiple commands in one list if that is desired. 
        if bench_type.lower() == 'mix': self.benchmarks = ['mixgraph']
        elif bench_type.lower() == 'random': self.benchmarks = ['readrandom']
        elif bench_type.lower() == 'ycsb': 
            self.__ycsb = True
            if 'ycsb_workload' in options: self.__ycsb_workload = options['ycsb_workload'].lower()

        if 'output_file' in options: self.__output_file = options['output_file']
        if 'testing' in options: self.__testing = True
        if 'baseline' in options: self.__baseline = int(options['baseline'])


    def load_knob_configurations(self, knobs):
        """
        Adds the knob configurations for a benchmark run
        Each knob has a valid name as the key and value

        Arguments:
            knobs -> key-value pairs of knobs to tune
        """
        self.knobs = knobs
        if len(self.__output_file) > 0:
            with open(self.__output_file, 'a') as file:
                file.write('\n\nBenchmark with knobs: ' + str(self.knobs) + '  ')


    def add_command_options(self, options_file=False):
        result = ''
        if options_file or self.__ycsb:
            file_path = config.YCSB_OPTIONS_FILE if self.__ycsb else config.OPTIONS_FILE
            template_path = config.YCSB_OPTIONS_FILE_TEMPLATE if self.__ycsb else config.OPTIONS_FILE_TEMPLATE
            # Read options_file parameters and find alter coresponding knobs.
            with open(template_path, 'r') as file:
                data = file.readlines()
                for i, line in enumerate(data):
                    if '=' in line.strip():
                        kv_pair = line.strip()
                        key, value = kv_pair.split('=', 1)
                        if key in self.knobs:
                            data[i] = '  ' + key + '=' + self.knobs[key] + '\n'

            # Finally, write the new data
            with open(file_path, 'w') as file:
                file.writelines(data)

            # Add options file to command
            if self.__ycsb:
                result += f' -p rocksdb.optionsfile={file_path}'
            else:
                result += f' options_file={file_path}'

        else: # We provide command line flags instead.    
            if len(self.knobs.keys()) > 0:
                for knob in self.knobs:
                    result += f' --{knob}={self.knobs[knob]}'
            
        return result


    def run_filling(self, fill_type='random', num_million=50, options_file=False):
        """
        Create and fill a database instance with key-value pairs

        Arguments:
            fill_type -> random (default) or seq (sequential)
            num_million -> number of million key-value pairs to fill
        """
        if self.__ycsb:
            command = f'{config.YCSB_PATH}bin/ycsb.sh load rocksdb -s -P {config.YCSB_PATH}workloads/workload{self.__ycsb_workload} -P {config.YCSB_PROPERTIES_FILE} -p rocksdb.dir={config.DB_DIR_YCSB}'
        else:
            command = f'{config.BENCHMARK_COMMAND_PATH} -db={config.DB_DIR} --benchmarks="fill{fill_type}" -num={num_million*1000000}'

        command += self.add_command_options(options_file) # We're not tuning knobs with an options
        
        try:
            subprocess.run(command, shell=True)
        except CalledProcessError:
            print('Error running the filling benchmark, please check the command format and paths given.')


    def run_benchmark(self, runs=1, num_million=1, fill=False, options_file=False):
        """
        Run a benchmark and parse the throughput results.
        """
        if self.__ycsb:
            command = f'{config.YCSB_PATH}bin/ycsb.sh run rocksdb -s -P {config.YCSB_PATH}workloads/workload{self.__ycsb_workload} -P {config.YCSB_PROPERTIES_FILE} -p rocksdb.dir={config.DB_DIR_YCSB}'
        else:
            benchmarks = f'"{",".join(self.benchmarks)}"'
            command = f'{config.BENCHMARK_COMMAND_PATH} -db={config.DB_DIR} --benchmarks={benchmarks}'
            if 'mixgraph' in benchmarks:
                command += (' use_direct_io_for_flush_and_compaction=true -use_direct_reads=true ' 
                            '-cache_size=268435456 -keyrange_dist_a=14.18 -keyrange_dist_b=-2.917 ' 
                            '-keyrange_dist_c=0.0164 -keyrange_dist_d=-0.08082 -keyrange_num=30 '
                            '-value_k=0.2615 -value_sigma=25.45 -iter_k=2.517 -iter_sigma=14.236 '
                            '-mix_get_ratio=0.85 -mix_put_ratio=0.14 -mix_seek_ratio=0.01 '
                            '-sine_mix_rate_interval_milliseconds=5000 -sine_a=1000 '
                            '-sine_b=0.000000073 -sine_d=4500000 --perf_level=1 -reads=4200000 '
                            '-num=50000000 -key_size=48 --statistics=1 --duration=300')
        
        command += self.add_command_options(options_file)

        throughput = 0

        try:
            results = [] # Save to later calculate average
            for _ in range(runs):
                print(command)
                if self.__ycsb:
                    try:
                        subprocess.run(f'sudo rm -r {config.DB_DIR_YCSB}')
                    except FileNotFoundError:
                        pass
                    self.run_filling(fill_type='random')
                else:
                    if fill:
                        self.run_filling(fill_type='random',num_million=num_million, options_file=options_file)
                        command += ' --use_existing_db'
                for line in subprocess.check_output(command, shell=True, universal_newlines=True).split('\n'):
                    if self.__ycsb:
                        if 'OVERALL' in str(line):
                            match = re.search('\d+[.]\d+', line)
                            if match is not None:
                                throughput = match.group(0)
                                print(throughput)
                                results.append(float(throughput))
                                if len(self.__output_file) > 0:
                                    with open(self.__output_file, 'a') as file:
                                        file.write(f'\nThroughput (ops/sec): {throughput}  ')
                    else:
                        if 'ops/sec;' in str(line):
                            print(str(line))
                            match = re.search('((\d+)\sops)', line)
                            throughput = match.group(2)
                            results.append(int(throughput))
                            if len(self.__output_file) > 0:
                                with open(self.__output_file, 'a') as file:
                                    file.write(f'\nThroughput (ops/sec): {throughput}  ')
            if self.__testing:
                average = int(sum(results) / len(results))
                if not self.knobs:
                    self.__baseline = average
                if self.__baseline != 0:
                    deviation = ((average - self.__baseline) / self.__baseline) * 100
                else:
                    deviation = 0
                with open(self.__output_file, 'a') as file:
                    file.write(f'\nAverage (ops/sec): **{average}**  ')
                    file.write(f'\nDeviation from baseline: **{"{:.2f}".format(deviation)}%**  ')

        except CalledProcessError:
            print('Error running the benchmark, please check the command format and paths given.')

        return throughput