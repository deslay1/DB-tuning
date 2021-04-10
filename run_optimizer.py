"""
Runs a benchmark test using db_bench tool for RocksDB
"""
import subprocess
import re
import config

class Benchmark:
    def __init__(self, bench_type=None):
        self.knobs = {}
        self.benchmarks=[]

        # One can input multiple commands in one list if that is desired. 
        if bench_type == 'mix': self.benchmarks = ['mixgraph']
        elif bench_type == 'random': self.benchmarks = ['readrandom']

    def load_knob_configurations(self, knobs):
        """
        Adds the knob configurations for a benchmark run
        Each knob has a valid name as the key and value

        Arguments:
            knobs -> key-value pairs of knobs to tune
        """
        self.knobs = knobs


    def run_filling(self, fill_type='random', num_million=50):
        """
        Create and fill a database instance with key-value pairs

        Arguments:
            fill_type -> random (default) or seq (sequential)
            num_million -> number of million key-value pairs to fill
        """
        command = f'{config.BENCHMARK_COMMAND_PATH} --benchmarks="fill{fill_type}" -num={num_million*1000000}'

        if len(self.knobs.keys()) > 0:
            for knob in self.knobs:
                command += f' -{knob}={self.knobs[knob]}'
        
        try:
            subprocess.run(command, shell=True)
        except CalledProcessError:
            print('Error running the filling benchmark, please check the command format and paths given.')


    def run_benchmark(self):
        """
        Run a benchmark and parse the throughput results.
        """
        benchmarks = f'"{",".join(self.benchmarks)}"'

        command = f'{config.BENCHMARK_COMMAND_PATH} --benchmarks={benchmarks} --use-existing-db'
        
        if len(self.knobs.keys()) > 0:
            for knob in self.knobs:
                command += f' --{knob}={self.knobs[knob]}'

        try:
            subprocess.run(command, shell=True)
        except CalledProcessError:
            print('Error running the filling benchmark, please check the command format and paths given.')
        # result = subprocess.check_output(command, shell=True)
        for line in subprocess.check_output(command, shell=True, universal_newlines=True).split('\n'):
            if 'ops/sec;' in str(line):
                match = re.search('((\d+)\sops)', line)
                throughput = match.group(2)
                with open('internal_tool_test.txt', 'a') as file:
                    file.write(f'\nThroughput (ops/sec): {throughput}')

        print('\nDONE')


if __name__ == '__main__':
    bench = Benchmark(bench_type='random')
    # 0. Knob testing
    knobs = {
        'max_background_compactions': '64',
        'compaction_readahead_size': '2000000'
    }
    bench.load_knob_configurations(knobs)

    # 1. Fill with data
    bench.run_filling(num_million=1)

    # 2. Run benchmark
    for i in range(3):
        bench.run_benchmark()

    # 3. Make calls to the BO API and receive samples...
