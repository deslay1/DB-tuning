
from benchmark import RocksdbBenchmark
from hypermapper import optimizer


def run_benchmark(knobs):
    options = {
        'readwritepercent': 90,
        'threads': 32
    }
    bench = RocksdbBenchmark(
        bench_type='readrandomwriterandom', options=options)
    knobs = dict((k, str(v)) for k, v in knobs.items())
    bench.load_knob_configurations(knobs)
    throughput = bench.run_benchmark(
        runs=3, num_million=5, fill=True, options_file=False, use_existing=True, max_seconds=300)
    return -int(throughput)


# subprocess.run('sudo rm hypermapper_logfile.log', shell=True)
# subprocess.run('python setup_optimizer_config.py', shell=True)
optimizer.optimize("util/optimizer_scenario.json", run_benchmark)
