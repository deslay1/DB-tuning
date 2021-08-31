"""
Configuration file optimizer parameters and tuning knobs.
"""
import os
from datetime import datetime

ROOT = os.getcwd()

# RESULT_DIR = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

##########################################################
#               Hypermapper Configurations               #
##########################################################

OPTIMIZATION_OBJECTIVE = ["Throughput"]
APPLICATION_NAME = f"{OPTIMIZATION_OBJECTIVE[0]}_benchmark"

# 1. Feature importance
OPTIMIZATION_ITERATIONS = 1
NUMBER_OF_SAMPLES = 100
# NUMBER_OF_SAMPLES = len(INPUT_PARAMETERS) * 10  # 10D
# 2. BO
# OPTIMIZATION_ITERATIONS = 100 - \
#     (len(INPUT_PARAMETERS)+1)  # (50 - Number of samples)
# NUMBER_OF_SAMPLES = len(INPUT_PARAMETERS)+1  # D + 1

# Model
MODEL = "random_forest"
OUTPUT_IMAGE_FILE = f"image_output.pdf"

##########################################################
#            RocksDB Benchmark Configurations            #
##########################################################
DB_DIR = "/home/ubuntu/db-dir"

# OPTIONS_FILE = '/tmp/rocksdbtest-1002/dbbench/OPTIONS-000006'
OPTIONS_FILE = f"{ROOT}/util/rocksdb_option_files/options_file.ini"

# Default template caused by a fill random benchmark with 1M inserted kV-pairs
OPTIONS_FILE_TEMPLATE = (
    f"{ROOT}/util/rocksdb_option_files/options_file_template_default.ini"
)

BENCHMARK_COMMAND_PATH = f"{ROOT}/../rocksdb/db_bench"
BENCHMARK_TYPE = "readrandomwriterandom"

DB_DIR_YCSB = "/tmp/rocksdb-bench-ycsb"
YCSB_OPTIONS_FILE = f"{ROOT}/util/rocksdb_option_files/ycsb_options_file.ini"
YCSB_OPTIONS_FILE_TEMPLATE = (
    f"{ROOT}/util/rocksdb_option_files/ycsb_options_file_template_default.ini"
)
YCSB_PATH = f"{ROOT}/../ycsb-0.17.0/"
YCSB_PROPERTIES_FILE = f"{ROOT}/util/ycsb_properties.dat"

##########################################################
#                     Tuning Knobs                       #
##########################################################
Knobs = {}

# Knob ref: from 1 to 5*10^5
Knobs["block_size"] = {}
Knobs["block_size"]["parameter_default"] = 4096  # 2^12
Knobs["block_size"]["parameter_type"] = "ordinal"
Knobs["block_size"]["values"] = [2 ** 0] + [
    2 ** x for x in range(2, 20, 1)
]  # Highest value 2^19 = 524 288

# categorical, may or may not have a large impact
Knobs["cache_index_and_filter_blocks"] = {}
Knobs["cache_index_and_filter_blocks"]["parameter_default"] = "false"
Knobs["cache_index_and_filter_blocks"]["parameter_type"] = "categorical"
Knobs["cache_index_and_filter_blocks"]["values"] = ["false", "true"]

# self-defined range: 0 to 4*10^6
Knobs["compaction_readahead_size"] = {}
Knobs["compaction_readahead_size"]["parameter_default"] = 0  # 2^12
Knobs["compaction_readahead_size"]["parameter_type"] = "ordinal"
Knobs["compaction_readahead_size"]["values"] = [40000 * x for x in range(0, 11)]

# categorical, may or may not have a large impact,
# According to https://github.com/facebook/rocksdb/wiki/compression_type, LZ4 is almost always better than default
# NOTE: this this format when passing command line flags rather than an options file.
# With an options file, the values are formulated differently, for exmplle 'LZ4' --> 'kLZ4compression_type'
Knobs["compression_type"] = {}
Knobs["compression_type"]["parameter_default"] = "snappy"
Knobs["compression_type"]["parameter_type"] = "categorical"
# see link above, these are the most relevant
Knobs["compression_type"]["values"] = ["snappy", "zstd", "lz4"]

# Knob ref: from 1 to 2^8
Knobs["level0_file_num_compaction_trigger"] = {}
Knobs["level0_file_num_compaction_trigger"]["parameter_default"] = 4
Knobs["level0_file_num_compaction_trigger"]["parameter_type"] = "ordinal"
Knobs["level0_file_num_compaction_trigger"]["values"] = [2 ** x for x in range(0, 9)]

# Knob ref: from 1 to 2^10
Knobs["level0_slowdown_writes_trigger"] = {}
Knobs["level0_slowdown_writes_trigger"]["parameter_default"] = 20  # old: 0
Knobs["level0_slowdown_writes_trigger"]["parameter_type"] = "ordinal"
Knobs["level0_slowdown_writes_trigger"]["values"] = sorted(
    [0, 20] + [2 ** x for x in range(0, 11)]
)

# Knob ref: from 1 to 2^10
Knobs["level0_stop_writes_trigger"] = {}
Knobs["level0_stop_writes_trigger"]["parameter_default"] = 36  # old: 32
Knobs["level0_stop_writes_trigger"]["parameter_type"] = "ordinal"
Knobs["level0_stop_writes_trigger"]["values"] = sorted(
    [36] + [2 ** x for x in range(0, 11)]
)

# Knob ref: from 1 to 2^8
Knobs["max_background_compactions"] = {}
Knobs["max_background_compactions"]["parameter_default"] = -1  # old: 1
Knobs["max_background_compactions"]["parameter_type"] = "ordinal"
Knobs["max_background_compactions"]["values"] = sorted(
    [-1] + [2 ** x for x in range(0, 9)]
)

# Knob ref: from 1 to 10
Knobs["max_background_flushes"] = {}
Knobs["max_background_flushes"]["parameter_default"] = -1  # old: 1
Knobs["max_background_flushes"]["parameter_type"] = "integer"
Knobs["max_background_flushes"]["values"] = [-1, 10]

# Knob ref: from 5 to 15
Knobs["max_bytes_for_level_multiplier"] = {}
Knobs["max_bytes_for_level_multiplier"]["parameter_default"] = 10
Knobs["max_bytes_for_level_multiplier"]["parameter_type"] = "integer"
Knobs["max_bytes_for_level_multiplier"]["values"] = [5, 15]

# Knob ref: from 1 to 2^7
Knobs["max_write_buffer_number"] = {}
Knobs["max_write_buffer_number"]["parameter_default"] = 2
Knobs["max_write_buffer_number"]["parameter_type"] = "ordinal"
Knobs["max_write_buffer_number"]["values"] = [2 ** x for x in range(0, 8)]

# Knob ref: from 1 to 2^5
Knobs["min_write_buffer_number_to_merge"] = {}
Knobs["min_write_buffer_number_to_merge"]["parameter_default"] = 1
Knobs["min_write_buffer_number_to_merge"]["parameter_type"] = "ordinal"
Knobs["min_write_buffer_number_to_merge"]["values"] = [2 ** x for x in range(0, 6)]

# Knob ref: from 1 to 15*10^7
Knobs["write_buffer_size"] = {}
Knobs["write_buffer_size"]["parameter_default"] = 2 ** 26
Knobs["write_buffer_size"]["parameter_type"] = "ordinal"
Knobs["write_buffer_size"]["values"] = [2 ** 0] + [2 ** x for x in range(2, 31, 1)]

