"""
Runs a benchmark test using db_bench tool for RocksDB
"""
from Benchmark import RocksdbBenchmark

def mixgraph_test():
    options = {
        # 'output_file': 'outputs/random_test.md',
        'output_file': 'outputs/mixgraph_test_filling.md',
        # 'ycsb_workload': 'b'
    }
    bench = RocksdbBenchmark(bench_type='mix', options=options)
    knobs = {
    }
    bench.load_knob_configurations(knobs)
    bench.run_filling(fill_type='random',num_million=50, options_file=True)
    bench.run_benchmark(runs=1, options_file=True)

    knobs = {
        'max_background_compactions': '64',
        # 'compaction_readahead_size': '2000000',
        # 'level0_slowdown_writes_trigger': '24',
        # 'level0_stop_writes_trigger': '40',
        # 'write_buffer_size': '256',
        # 'optimize_filters_for_hits': 'True',
        'block_size': '64',
    }
    bench.load_knob_configurations(knobs)
    bench.run_benchmark(runs=1, options_file=True)

    knobs = {
        'max_background_compactions': '64',
        # 'compaction_readahead_size': '2000000',
        # 'level0_slowdown_writes_trigger': '1024',
        # 'write_buffer_size': '268435456',
        'block_size': str(2**16),
    }
    bench.load_knob_configurations(knobs)
    bench.run_benchmark(runs=1, options_file=True)


if __name__ == '__main__':
    mixgraph_test()
    # options = {
    #     'output_file': 'outputs/mixgraph_test.md',
    #     # 'ycsb_workload': 'b'
    # }

    # bench = RocksdbBenchmark(bench_type='mix', options=options)
    # bench = RocksdbBenchmark(bench_type='random', options=options)
    # bench = RocksdbBenchmark(bench_type='ycsb', options)

    # 1. Load knobs
    # bench.load_knob_configurations(knobs)

    # 2. Fill with data, probably not a good a good idea to run if we run a 'mix' benchmark type
    # bench.run_filling(num_million=1)

    # 3. Run benchmark (throughput result should be returned for step 4.)
    # bench.run_benchmark(runs=3, options_file=True)

    # 4. Make calls to the BO API and receive samples...
