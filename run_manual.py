from benchmark import RocksdbBenchmark


options = {
    'output_file': 'latencies.md',
    # 'testing': True,
    'readwritepercent': 50,
    'threads': 32
}
bench = RocksdbBenchmark(bench_type='readrandomwriterandom', options=options)

knob_tests = [
    {},
    {
        'block_size': '4096',
        'cache_index_and_filter_blocks': 'false',
        'compaction_readahead_size': '0',
        'compression_type': 'snappy',
        'level0_file_num_compaction_trigger': '4',
        'level0_slowdown_writes_trigger': '0',
        'level0_stop_writes_trigger': '32',
        'max_background_compactions': '1',
        'max_background_flushes': '1',
        'max_bytes_for_level_multiplier': '10',
        'write_buffer_size': '67108864',
    },
]
for knobs in knob_tests:
    bench.load_knob_configurations(knobs)
    tps, rl, wl = bench.run_benchmark(runs=3, num_million=5, fill=True,
                                      options_file=False, use_existing=True, calc_latency=True)
    print(tps)
    print(rl)
    print(wl)
