import os
import json
import config
from benchmark_commands import run_sequential_random
from datetime import datetime

def create_json(filename='example_config_hm'):
    """
    Creates a json file for usage by the optimizer service
    """

    scenario = {}
    scenario['application_name'] = config.APPLICATION_NAME
    scenario['optimization_objectives'] = config.OPTIMIZATION_OBJECTIVE
    scenario['optimization_iterations'] = config.OPTIMIZATION_ITERATIONS
    scenario['models'] = {}
    scenario['models']['model'] = config.MODEL
    scenario['design_of_experiment'] = {}
    scenario['design_of_experiment']['number_of_samples'] = config.NUMBER_OF_SAMPLES
    scenario['input_parameters'] = {}
    scenario['output_data_file'] = '{}_output.csv'.format(
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    with open('search_space.json', 'r') as fobj:
        knobs = json.load(fobj)

    # scenario['input_parameters'] = {}
    parameter_options = ['parameter_default', 'parameter_type', 'values']
    for para in config.INPUT_PARAMETERS:
        scenario['input_parameters'][para] = dict(
            zip(parameter_options, [knobs[para][k] for k in parameter_options]))

    with open(filename, 'w') as scenario_file:
        json.dump(scenario, scenario_file, indent=4)


def run_benchmark():
    """
    Runs a benchmark test using db_bench tool for RocksDB
    """
    run_sequential_random()


if __name__ == '__main__':
    create_json('optimizer_scenario.json')
    # run_benchmark()
