from Benchmark import RocksdbBenchmark

def mixgraph_test(label, threads):
    options = {
        'threads': threads,
        # 'output_file': 'outputs/mixgraph_test_no_filling.md',
        'output_file': f'outputs/mixgraph_{label}.md',
        # 'output_file': f'outputs/random_{label}.md',
        'testing': True,
        # 'baseline': '70229'
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
        {'max_background_compactions': '64'},
        {
            'max_background_compactions': '64',
            'level0_file_num_compaction_trigger': '8',
        },
        {
            'max_background_compactions': '64',
            'level0_file_num_compaction_trigger': '8',
            'write_buffer_size': str(2**28),
        },
        # {'write_buffer_size': str(2**18)},
        # {'write_buffer_size': str(2**28)},
        # {'block_size': str(2**2)},
        # {'block_size': str(2**18)},
        # {'level0_slowdown_writes_trigger': '8'},
        # {'level0_slowdown_writes_trigger': '24'},
    ]
    # threads = [8, 16, 32]
    for knobs in knob_tests:
        bench.load_knob_configurations(knobs)
        # for t in threads:
        bench.run_benchmark(runs=2, num_million=50, fill=True, options_file=False)
            # bench.change_threads(t)


def ycsb_test():
    options = {
        'output_file': 'outputs/ycsb_test.md',
        'ycsb_workload': 'a',
        'threads': 1
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
        for i in range(1, 8, 3):
            bench.run_benchmark(runs=1, fill=True, options_file=False)
            bench.change_threads(2*i)
        # bench.run_benchmark(runs=3)

if __name__ == '__main__':
    mixgraph_test('filling_april_26', 1)
    # mixgraph_test('50M_threading32',32)
    # ycsb_test()