from hypermapper import optimizer
from project.benchmark import RocksdbBenchmark
import project.config as config
import subprocess
import pandas as pd
import pdb

def run_default():
    options = {
        'output_file': 'test.md',
        # 'testing': True,
        'threads': 32
    }
    bench = RocksdbBenchmark(bench_type='readrandomwriterandom', options=options)

    for _ in range(1):
        tps, l = bench.run_benchmark(runs=3, num_million=5, fill=True,
                                    options_file=False, use_existing=True, max_seconds=300, calc_latency=True)
        print(tps)
        print(l)


def run_from_configs():
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
        # [
        #     '1024,false,360000,snappy,1,8,16,8,0,0,1073741824',
        #     '4096,false,320000,lz4,2,2,64,128,6,3,1073741824',
        #     '2048,false,240000,lz4,2,1024,8,8,5,2,1073741824',
        # ],
        # 50-50
        [
            '8,false,360000,snappy,1,512,16,256,4,4,134217728',
            '32,false,400000,zstd,16,8,4,2,0,4,268435456',
            '512,false,40000,lz4,1,2,32,64,5,10,67108864',
        ],
        # 90-10
        # [
        #     '1024,false,360000,snappy,1,32,16,64,8,13,268435456',
        #     '16,false,120000,snappy,1,2,128,1,10,4,1073741824',
        #     '512,false,240000,snappy,1,4,256,32,5,0,1073741824',
        # ]
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


def run_hypermapper_from_configs():

    run_ind = 0
    config_index = 0

    def run_benchmark(knobs):
        options = {
            'output_file': f'snic-test/RUN_1_{run_ind}.csv',
            'readwritepercent': 50,
            'threads': 32
        }
        bench = RocksdbBenchmark(
            bench_type='readrandomwriterandom', options=options)
        # knobs are input from hypermapper optimizer - but ignore and change them since we are going to get them from a file for RUN_1
        df = pd.read_csv('snic-test/2021-07-04_20-57-17_output.csv', sep=',')
        knob_configs = df[config.INPUT_PARAMETERS]
        knobs = knob_configs.iloc[config_index].to_dict()
        if config_index == 100: 
            config_index = 0
        else:
            config_index += 1
        knobs = dict((k, str(v)) for k, v in knobs.items())
        bench.load_knob_configurations(knobs)
        throughput, _ = bench.run_benchmark(
            runs=3, num_million=5, fill=True, options_file=False, use_existing=True, max_seconds=300, calc_latency=True)
        return -int(throughput)

    for _ in range(10):
        run_ind += 1
        config_index = 0
        subprocess.run('python setup_optimizer_config.py', shell=True)
        optimizer.optimize("util/optimizer_scenario.json", run_benchmark)


def run_hypermapper():
    run_ind = 0

    def run_benchmark(knobs):
        options = {
            'output_file': f'snic-test/RUN_{run_ind}.csv',
            'readwritepercent': 50,
            'threads': 32
        }
        bench = RocksdbBenchmark(
            bench_type='readrandomwriterandom', options=options)
        knobs = dict((k, str(v)) for k, v in knobs.items())
        bench.load_knob_configurations(knobs)
        throughput, _ = bench.run_benchmark(
            runs=3, num_million=5, fill=True, options_file=False, use_existing=True, max_seconds=300, calc_latency=True)
        return -int(throughput)


    # subprocess.run('sudo rm hypermapper_logfile.log', shell=True)
    for _ in range(10):
        run_ind += 1
        subprocess.run('python setup_optimizer_config.py', shell=True)
        optimizer.optimize("util/optimizer_scenario.json", run_benchmark)


def run_manual():
    options = {
        'output_file': 'latencies.md',
        # 'testing': True,
        'readwritepercent': 50,
        'threads': 32
    }
    bench = RocksdbBenchmark(bench_type='readrandomwriterandom', options=options)

    knob_tests = [
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
        tps, l = bench.run_benchmark(runs=3, num_million=5, fill=True,
                                    options_file=False, use_existing=True, max_seconds=300, calc_latency=True)
        print(tps)
        print(l)
