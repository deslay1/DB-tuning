from benchmark import RocksdbBenchmark


options = {
    'threads': 1,
    'output_file': 'mixgraph_1.md',
    'testing': True,
    'readwritepercent': 50,
}
bench = RocksdbBenchmark(bench_type='readrandomwriterandom', options=options)
knob_tests = [
    {},
    # {'max_background_compactions': '64'},
    # {
    #     'max_background_compactions': '64',
    #     'level0_file_num_compaction_trigger': '8',
    # },
    # {
    #     'max_background_compactions': '64',
    #     'level0_file_num_compaction_trigger': '8',
    #     'write_buffer_size': str(2**28),
    # },
    # {'write_buffer_size': str(2**18)},
    # {'write_buffer_size': str(2**28)},
    # {'block_size': str(2**2)},
    # {'block_size': str(2**18)},
    # {'level0_slowdown_writes_trigger': '8'},
    # {'level0_slowdown_writes_trigger': '24'},
]
for knobs in knob_tests:
    bench.load_knob_configurations(knobs)
    bench.run_benchmark(runs=1, num_million=5, fill=True,
                        options_file=False, use_existing=True, max_seconds=300)
