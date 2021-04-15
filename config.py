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
INPUT_PARAMETERS = ['block_size', 'level0_slowdown_writes_trigger', 'level0_stop_writes_trigger', 'max_background_compactions', 'max_background_flushes', 'write_buffer_size']
# Model
MODEL = 'random_forest'

##########################################################
#               RocksDB Configurations                #
##########################################################
DB_DIR = '/tmp/rocksdb-bench'
# OPTIONS_FILE = '/tmp/rocksdbtest-1002/dbbench/OPTIONS-000006'
OPTIONS_FILE = 'util/options_file.ini'
OPTIONS_FILE_TEMPLATE = 'util/options_file_template_default.ini' # Default template caused by a fill random benchmark with 1M inserted kV-pairs
BENCHMARK_COMMAND_PATH = '/home/osama_eldawebi/main/rocksdb/db_bench'
YCSB_PATH = '/home/osama_eldawebi/main/ycsb-0.17.0/'

##########################################################
#                     Tuning Knobs                    #
##########################################################
Knobs = {}

# Knob ref: from 1 to 5*10^5
Knobs['block_size'] = {}
Knobs['block_size']['parameter_default'] = 4096 # 2^12
Knobs['block_size']['parameter_type'] = 'ordinal'
Knobs['block_size']['values'] = [2**0] + [2**x for x in range(1, 20, 2)] # Highest value 2^19 = 524 288

# Knob ref: from 1 to 2^10
Knobs['level0_slowdown_writes_trigger'] = {}
Knobs['level0_slowdown_writes_trigger']['parameter_default'] = 0
Knobs['level0_slowdown_writes_trigger']['parameter_type'] = 'ordinal'
Knobs['level0_slowdown_writes_trigger']['values'] = [2**x for x in range(0, 11)]

# Knob ref: from 1 to 2^10
Knobs['level0_stop_writes_trigger'] = {}
Knobs['level0_stop_writes_trigger']['parameter_default'] = 36
Knobs['level0_stop_writes_trigger']['parameter_type'] = 'ordinal'
Knobs['level0_stop_writes_trigger']['values'] = [2**x for x in range(0, 11)]

# Knob ref: from 1 to 2^8
Knobs['max_background_compactions'] = {}
Knobs['max_background_compactions']['parameter_default'] = 1
Knobs['max_background_compactions']['parameter_type'] = 'ordinal'
Knobs['max_background_compactions']['values'] = [2**x for x in range(0, 9)]

# Knob ref: from 1 to 10
Knobs['max_background_flushes'] = {}
Knobs['max_background_flushes']['parameter_default'] = 1
Knobs['max_background_flushes']['parameter_type'] = 'integer'
Knobs['max_background_flushes']['values'] = [x for x in range(1, 11)]

# Knob ref: from 1 to 15*10^7
Knobs['write_buffer_size'] = {}
Knobs['write_buffer_size']['parameter_default'] = 2**26
Knobs['write_buffer_size']['parameter_type'] = 'ordinal'
Knobs['write_buffer_size']['values'] = [2**0] + [2**x for x in range(1, 29, 4)]


if __name__ == '__main__':
    with open('util/search_space.json', 'w') as file:
        json.dump(Knobs, file, indent=4)
