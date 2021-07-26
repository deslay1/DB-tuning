import os
import json
import config
from datetime import datetime


def create_json(filename='example_scenario.json'):
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
    scenario['design_of_experiment']['doe_type'] = 'standard latin hypercube'
    scenario['design_of_experiment']['number_of_samples'] = config.NUMBER_OF_SAMPLES
    scenario['input_parameters'] = {}
    scenario['print_parameter_importance'] = True
    scenario['output_data_file'] = 'snic-test/{}_output.csv'.format(
        datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    scenario['output_image'] = {
        'output_image_pdf_file': config.OUTPUT_IMAGE_FILE,
        'optimization_objectives_labels_image_pdf': ['Throughput (ops/sec)'],
        # 'image_xlog': False,
        # 'image_ylog': True,
    }

    # Load knobs
    with open('util/search_space.json', 'r') as fobj:
        knobs = json.load(fobj)

    # Write knobs to file
    parameter_options = ['parameter_default', 'parameter_type', 'values']
    for para in config.INPUT_PARAMETERS:
        scenario['input_parameters'][para] = dict(
            zip(parameter_options, [knobs[para][k] for k in parameter_options]))

    with open(filename, 'w') as scenario_file:
        json.dump(scenario, scenario_file, indent=4)


if __name__ == '__main__':
    config.update_config()
    create_json('util/optimizer_scenario.json')
