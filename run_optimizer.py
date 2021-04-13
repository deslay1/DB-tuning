"""
Runs a benchmark test using db_bench tool for RocksDB
"""
import subprocess
import re
import config

class Benchmark:
    def __init__(self, bench_type=None, options={}):
        """
        RocksDB benchmark class.

        bench_type -> The following benchmark types are supported:
            'mix' -> 'migraph' with 78% GET, 13% PUT, 6% DELETE, 3% Iterate.
            'random' -> 'readrandom' with only read operations of keys in random order.
            'ycsb' ->  Run a YCSB benchmark. Default workload is A unless specified by in the options argument.
        
        options -> Additional options can be provided:
            '{ycsb_workload : <workload_type}' -> workload_type: one of: <a,b,c,d,e,f>
        """
        self.knobs = {}
        self.benchmarks=[]
        self.__filling_done = False
        self.__ycsb = False
        self.__ycsb_workload = 'a'

        # One can input multiple commands in one list if that is desired. 
        if bench_type.lower() == 'mix': self.benchmarks = ['mixgraph']
        elif bench_type.lower() == 'random': self.benchmarks = ['readrandom']
        elif bench_type.lower() == 'ycsb': 
            self.__ycsb = True
            if 'ycsb_workload' in options: self.__ycsb_workload = options['ycsb_workload'].lower()

    def load_knob_configurations(self, knobs):
        """
        Adds the knob configurations for a benchmark run
        Each knob has a valid name as the key and value

        Arguments:
            knobs -> key-value pairs of knobs to tune
        """
        self.knobs = knobs


    def add_command_options(self, options_file=False):
        result = ''
        if options_file or self.__ycsb:

            # Read options_file parameters and find alter coresponding knobs.
            with open(config.OPTIONS_FILE_TEMPLATE, 'r') as file:
                data = file.readlines()
                for i, line in enumerate(data):
                    if '=' in line.strip():
                        kv_pair = line.strip()
                        key, value = kv_pair.split('=', 1)
                        if key in self.knobs:
                            data[i] = '  ' + key + '=' + self.knobs[key] + '\n'
                            print(data[i])

            # Finally, write the new data
            with open(config.OPTIONS_FILE, 'w') as file:
                file.writelines(data)

            # Add options file to command
            if self.__ycsb:
                result += f' -p rocksdb.optionsfile={config.OPTIONS_FILE}'
            else:
                result += f' options_file={config.OPTIONS_FILE}'

        else: # We provide command line flags instead.    
            if len(self.knobs.keys()) > 0:
                for knob in self.knobs:
                    result += f' --{knob}={self.knobs[knob]}'
            
        return result


    def run_filling(self, fill_type='random', num_million=50):
        """
        Create and fill a database instance with key-value pairs

        Arguments:
            fill_type -> random (default) or seq (sequential)
            num_million -> number of million key-value pairs to fill
        """
        if self.__ycsb:
            command = f'{config.YCSB_PATH}bin/ycsb.sh load rocksdb -s -P {config.YCSB_PATH}workloads/workload{self.__ycsb_workload} -p rocksdb.dir={config.DB_DIR}'
        else:
            command = f'{config.BENCHMARK_COMMAND_PATH} -db={config.DB_DIR} --benchmarks="fill{fill_type}" -num={num_million*1000000}'

        command += self.add_command_options()
        
        try:
            subprocess.run(command, shell=True)
        except CalledProcessError:
            print('Error running the filling benchmark, please check the command format and paths given.')

        self.__filling_done = True


    def run_benchmark(self, options_file=False):
        """
        Run a benchmark and parse the throughput results.
        """
        if self.__ycsb:
            command = f'{config.YCSB_PATH}bin/ycsb.sh run rocksdb -s -P {config.YCSB_PATH}workloads/workload{self.__ycsb_workload} -p rocksdb.dir={config.DB_DIR}'
        else:
            benchmarks = f'"{",".join(self.benchmarks)}"'
            command = f'{config.BENCHMARK_COMMAND_PATH} -db={config.DB_DIR} --benchmarks={benchmarks}'
            if self.__filling_done: command += ' --use_existing_db'
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

        try:
            for line in subprocess.check_output(command, shell=True, universal_newlines=True).split('\n'):
                if self.__ycsb:
                    if 'OVERALL' in str(line):
                        match = re.search('\d+[.]\d+', line)
                        if match is not None:
                            throughput = match.group(0)
                            with open('outputs/YCSB_test.txt', 'a') as file:
                                file.write(f'\nThroughput (ops/sec): {throughput}')
                else:
                    if 'ops/sec;' in str(line):
                        match = re.search('((\d+)\sops)', line)
                        throughput = match.group(2)
                        with open('outputs/internal_tool_test.txt', 'a') as file:
                            file.write(f'\nThroughput (ops/sec): {throughput}')

        except CalledProcessError:
            print('Error running the benchmark, please check the command format and paths given.')

        print('\nDONE')


if __name__ == '__main__':
    # bench = Benchmark(bench_type='mix')
    bench = Benchmark(bench_type='random')
    # bench = Benchmark(bench_type='ycsb', options={'ycsb_workload': 'c'})

    # 0. Knob testing
    knobs = {
        'max_background_compactions': '64',
        'compaction_readahead_size': '2000000'
    }
    bench.load_knob_configurations(knobs)

    # 1. Fill with data, probably nota good a good idea to run if we run a 'mix' benchmark type
    bench.run_filling(num_million=1)
    # bench.run_filling()

    # 2. Run benchmark
    for i in range(3):
        bench.run_benchmark(options_file=True)
        # bench.run_benchmark()

    # 3. Make calls to the BO API and receive samples...
