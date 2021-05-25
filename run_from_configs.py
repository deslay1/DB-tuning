from benchmark import RocksdbBenchmark


options = {
    'output_file': 'manual-results/latencies.md',
    'readwritepercent': 50,
    'threads': 32
}
bench = RocksdbBenchmark(bench_type='readrandomwriterandom', options=options)


# Parameters
keys = ['block_size', 'cache_index_and_filter_blocks', 'compaction_readahead_size',
        'compression_type', 'level0_file_num_compaction_trigger',
        'level0_slowdown_writes_trigger', 'level0_stop_writes_trigger',
        'max_background_compactions',
        'max_background_flushes', 'max_bytes_for_level_multiplier',
        'write_buffer_size']

# Configurations
workload_configs = [
    # 10-90
    [
        '1024,false,360000,snappy,1,8,16,8,0,0,1073741824',
        '4096,false,320000,lz4,2,2,64,128,6,3,1073741824',
        '2048,false,240000,lz4,2,1024,8,8,5,2,1073741824',
    ],
    # 50-50
    [
        '8,false,360000,snappy,1,512,16,256,4,4,134217728',
        '32,false,400000,zstd,16,8,4,2,0,4,268435456',
        '512,false,40000,lz4,1,2,32,64,5,10,67108864',
    ],
    # 90-10
    [
        '1024,false,360000,snappy,1,32,16,64,8,13,268435456',
        '16,false,120000,snappy,1,2,128,1,10,4,1073741824',
        '512,false,240000,snappy,1,4,256,32,5,0,1073741824',
    ]
]
knob_tests = []
for w in workload_configs:
    for config in w:
        values = config.split(',')
        knobs = {}
        for i, key in enumerate(keys):
            knobs[key] = values[i]
        knob_tests.append(knobs)

for knobs in knob_tests:
    bench.load_knob_configurations(knobs)
    tps, rl, wl = bench.run_benchmark(
        runs=3, num_million=5, fill=True, options_file=False, use_existing=True, max_seconds=300, calc_latency=True)
    print(tps)
    print(rl)
    print(wl)
