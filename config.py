"""
Configuration file optimizer parameters and tuning knobs.
"""
import json
# RESULT_DIR = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

##########################################################
#               Hypermapper Configurations               #
##########################################################
# Optimization objective ('Throughput' or 'Latency')
OPTIMIZATION_OBJECTIVE = ['Throughput']
OPTIMIZATION_ITERATIONS = 18
APPLICATION_NAME = f'{OPTIMIZATION_OBJECTIVE[0]}_benchmark'
# Design_of_experiment
NUMBER_OF_SAMPLES = 2
# Input parameters
INPUT_PARAMETERS = ['knob1']
# Model
MODEL = 'random_forest'

##########################################################
#               RocksDB Configurations                #
##########################################################
DB_DIR = '/tmp/rocksdb-bench'
OPTIONS_FILE = ''
BENCHMARK_COMMAND_PATH = '/home/osama_eldawebi/main/rocksdb/db_bench'

##########################################################
#                     Tuning Knobs                    #
##########################################################
Knobs = {}
# Knob 1
Knobs['knob1'] = {}
Knobs['knob1']['parameter_default'] = 4096
Knobs['knob1']['parameter_type'] = 'ordinal'
Knobs['knob1']['values'] = [640, 768, 896, 1024,
                            1280, 1536, 1792, 2048, 2560, 3072, 3584, 4096]
Knobs['knob1']['unit'] = 'MB'

# Add knobs to tune and there corresponding search space in the form same as above. Run knobs_search_space.py

if __name__ == '__main__':
    with open('search_space.json', 'w') as file:
        json.dump(Knobs, file, indent=4)
