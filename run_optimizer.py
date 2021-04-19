"""
Runs a benchmark test using db_bench tool for RocksDB
"""
from Benchmark import RocksdbBenchmark
from tests import *

from ax import optimize, SimpleExperiment, ChoiceParameter, SearchSpace, ParameterType, Arm, Models
import pandas as pd

    
def run_benchmark(parameters):
    options = {}
    bench = RocksdbBenchmark(bench_type='mix', options=options)
    knobs = dict((k, str(v)) for k, v in parameters.items())
    bench.load_knob_configurations(knobs)
    # bench.run_filling(fill_type='random',num_million=1, fill=True, options_file=True)
    throughput = bench.run_benchmark(runs=1, num_million=50, fill=False, options_file=True)
    return {'Throughput': (throughput, 0.0)}
        

def run_Ax_optimizer():
    best_parameters, best_values, experiment, model = optimize(
        parameters=[
            {
                'name': 'block_size',
                'type': 'choice',
                'values': [
                    1,
                    2,
                    8,
                    32,
                    128,
                    512,
                    2048,
                    8192,
                    32768,
                    131072,
                    524288
                ],
                'is_ordered': True,
                'value_type': 'int',
            },
            {
                'name': 'compaction_readahead_size',
                'type': 'choice',
                'values': [
                    0,
                    40000,
                    80000,
                    120000,
                    160000,
                    200000,
                    240000,
                    280000,
                    320000,
                    360000,
                    400000
                ],
                'is_ordered': True,
                'value_type': 'int',
            },
            {
                'name': 'level0_file_num_compaction_trigger',
                'type': 'choice',
                'values': [
                    1,
                    2,
                    4,
                    8,
                    16,
                    32,
                    64,
                    128,
                    256
                ],
                'is_ordered': True,
                'value_type': 'int',
            },
            {
                'name': 'max_background_compactions',
                'type': 'choice',
                'values': [
                    1,
                    2,
                    4,
                    8,
                    16,
                    32,
                    64,
                    128,
                    256
                ],
                'is_ordered': True,
                'value_type': 'int',
            },
            {
                'name': 'max_background_flushes',
                'type': 'choice',
                'values': [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    10
                ],
                'is_ordered': True,
                'value_type': 'int',
            },
            {
                'name': 'write_buffer_size',
                'type': 'choice',
                'values': [
                    1,
                    2,
                    32,
                    512,
                    8192,
                    131072,
                    2097152,
                    33554432
                ],
                'is_ordered': True,
                'value_type': 'int',
            },
            ],
        evaluation_function=run_benchmark,
        objective_name='Throughput',
        total_trials=100,
        # minimize=True,
        )
    return best_parameters, best_values


if __name__ == '__main__':
    # mixgraph_test()
    # ycsb_test()
    for _ in range(5):
        params, values = run_Ax_optimizer()
        with open('outputs/Ax_results.md', 'a') as file:
            file.write(f'\nBest parameters found: **{params}**  ')
            file.write(f'\nThroughput for above parameters: **{values}**  ')
    
    # param_1 = ChoiceParameter(name="block_size", values=[
    #                 1,
    #                 2,
    #                 8,
    #                 32,
    #                 128,
    #                 512,
    #                 2048,
    #                 8192,
    #                 32768,
    #                 131072,
    #                 524288
    #             ], parameter_type=ParameterType.INT)
    # param_2 = ChoiceParameter(name="compaction_readahead_size", values=[
    #                 0,
    #                 40000,
    #                 80000,
    #                 120000,
    #                 160000,
    #                 200000,
    #                 240000,
    #                 280000,
    #                 320000,
    #                 360000,
    #                 400000
    #             ], parameter_type=ParameterType.INT)
    # search_space = SearchSpace(
    # parameters=[param_1, param_2],
    # )
    # exp = SimpleExperiment(
    #     search_space=search_space,
    #     evaluation_function=run_benchmark,
    #     objective_name='Throughput',
    # )
    # exp.new_trial().add_arm(Arm(name='single_arm', parameters={'block_size': 1, 'compaction_readahead_size': 0}))
    # data = exp.fetch_data()

    # gpei = Models.BOTORCH(experiment=exp, data=data)
    # generator_run = gpei.gen(5)
    # exp.new_batch_trial(generator_run=generator_run)
    # print(data.df)
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
