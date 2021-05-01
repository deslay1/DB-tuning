import sys
import os
import config
from benchmark import RocksdbBenchmark
from hypermapper import optimizer

def run_benchmark(knobs):
    options = {
        'readwritepercent': 50
        'threads': 32
    }
    bench = RocksdbBenchmark(bench_type=config.BENCHMARK_TYPE, options=options)
    knobs = dict((k, str(v)) for k, v in knobs.items())
    bench.load_knob_configurations(knobs)
    throughput = bench.run_benchmark(runs=1, num_million=5, fill=True, options_file=False, use_existing=True, max_seconds=60)
    return -int(throughput)

optimizer.optimize("util/optimizer_scenario.json", run_benchmark)