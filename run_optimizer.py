"""
Runs a benchmark test using db_bench tool for RocksDB
"""
from Benchmark import RocksdbBenchmark

def mixgraph_test():
    options = {
        # 'output_file': 'outputs/mixgraph_test_no_filling.md',
        'output_file': 'outputs/mixgraph_test_filling.md',
        'baseline': '80876'
    }
    bench = RocksdbBenchmark(bench_type='mix', options=options)
    # knobs = {
        # 'max_background_compactions': '64',
        # 'compaction_readahead_size': '2000000',
        # 'level0_slowdown_writes_trigger': '24',
        # 'level0_stop_writes_trigger': '40',
        # 'write_buffer_size': '256',
        # 'optimize_filters_for_hits': 'True',
        # 'block_size': '64',
    # }
    knob_tests = [
        {},
        {'max_background_compactions': '16'},
        {'max_background_compactions': '64'},
        {'write_buffer_size': str(2**8)},
        {'write_buffer_size': str(2**28)},
        {'block_size': str(2**2)},
        {'block_size': str(2**18)},
        {'level0_slowdown_writes_trigger': '12'},
        {'level0_slowdown_writes_trigger': '24'},
    ]
    for knobs in knob_tests:
        bench.load_knob_configurations(knobs)
        # bench.run_filling(fill_type='random',num_million=1, fill=True, options_file=True)
        bench.run_benchmark(runs=3, num_million=50, fill=True, options_file=True)


def ycsb_test():
    options = {
        'output_file': 'outputs/ycsb_test.md',
        'ycsb_workload': 'a'
    }
    bench = RocksdbBenchmark(bench_type='ycsb', options=options)
    knob_tests = [
        {},
        {'max_background_compactions': '16'},
        {'max_background_compactions': '64'},
        {'write_buffer_size': str(2**8)},
        {'write_buffer_size': str(2**28)},
        {'block_size': str(2**2)},
        {'block_size': str(2**18)},
        {'level0_slowdown_writes_trigger': '12'},
        {'level0_slowdown_writes_trigger': '24'},
    ]
    for knobs in knob_tests:
        bench.load_knob_configurations(knobs)
        bench.run_benchmark(runs=3)


if __name__ == '__main__':
    # mixgraph_test()
    ycsb_test()
    # options = {
    #     'output_file': 'outputs/ycsb_test.md',
    #     'ycsb_workload': 'a'
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
