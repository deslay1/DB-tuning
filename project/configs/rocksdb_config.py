"""
Configuration file for RocksDB optimizer parameters and tuning knobs.
"""
import os

ROOT = os.getcwd()

##########################################################
#               Hypermapper Configurations               #
##########################################################

OPTIMIZATION_OBJECTIVE = ["Throughput"]
APPLICATION_NAME = f"{OPTIMIZATION_OBJECTIVE[0]}_benchmark"

# Model
MODEL = "random_forest"
OUTPUT_IMAGE_FILE = f"image_output.pdf"

##########################################################
#                Benchmark Configurations                #
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
#                     Tuning knobs                       #
##########################################################
knobs = {}

# Knob ref: from 1 to 5*10^5
knobs["block_size"] = {}
knobs["block_size"]["parameter_default"] = 4096  # 2^12
knobs["block_size"]["parameter_type"] = "ordinal"
knobs["block_size"]["values"] = [2 ** 0] + [
    2 ** x for x in range(2, 20, 1)
]  # Highest value 2^19 = 524 288

# categorical, may or may not have a large impact
knobs["cache_index_and_filter_blocks"] = {}
knobs["cache_index_and_filter_blocks"]["parameter_default"] = "false"
knobs["cache_index_and_filter_blocks"]["parameter_type"] = "categorical"
knobs["cache_index_and_filter_blocks"]["values"] = ["false", "true"]

# self-defined range: 0 to 4*10^6
knobs["compaction_readahead_size"] = {}
knobs["compaction_readahead_size"]["parameter_default"] = 0  # 2^12
knobs["compaction_readahead_size"]["parameter_type"] = "ordinal"
# knobs["compaction_readahead_size"]["values"] = [40000 * x for x in range(0, 11)]
knobs["compaction_readahead_size"]["values"] = [0]

# categorical, may or may not have a large impact,
# According to https://github.com/facebook/rocksdb/wiki/compression_type, LZ4 is almost always better than default
# NOTE: this this format when passing command line flags rather than an options file.
# With an options file, the values are formulated differently, for exmplle 'LZ4' --> 'kLZ4compression_type'
knobs["compression_type"] = {}
knobs["compression_type"]["parameter_default"] = "snappy"
knobs["compression_type"]["parameter_type"] = "categorical"
# see link above, these are the most relevant
# knobs["compression_type"]["values"] = ["snappy", "zstd", "lz4"]
knobs["compression_type"]["values"] = ["snappy"]

# Knob ref: from 1 to 2^8
knobs["level0_file_num_compaction_trigger"] = {}
knobs["level0_file_num_compaction_trigger"]["parameter_default"] = 4
knobs["level0_file_num_compaction_trigger"]["parameter_type"] = "ordinal"
knobs["level0_file_num_compaction_trigger"]["values"] = [2 ** x for x in range(0, 9)]

# Knob ref: from 1 to 2^10
knobs["level0_slowdown_writes_trigger"] = {}
knobs["level0_slowdown_writes_trigger"]["parameter_default"] = 20  # old: 0
knobs["level0_slowdown_writes_trigger"]["parameter_type"] = "ordinal"
# knobs["level0_slowdown_writes_trigger"]["values"] = sorted(
#     [0, 20] + [2 ** x for x in range(0, 11)]
# )
knobs["level0_slowdown_writes_trigger"]["values"] = [20]

# Knob ref: from 1 to 2^10
knobs["level0_stop_writes_trigger"] = {}
knobs["level0_stop_writes_trigger"]["parameter_default"] = 36  # old: 32
knobs["level0_stop_writes_trigger"]["parameter_type"] = "ordinal"
# knobs["level0_stop_writes_trigger"]["values"] = sorted(
#     [36] + [2 ** x for x in range(0, 11)]
# )
knobs["level0_stop_writes_trigger"]["values"] = [36]

# Knob ref: from 1 to 2^8
knobs["max_background_compactions"] = {}
knobs["max_background_compactions"]["parameter_default"] = -1  # old: 1
knobs["max_background_compactions"]["parameter_type"] = "ordinal"
knobs["max_background_compactions"]["values"] = sorted(
    [-1] + [2 ** x for x in range(0, 9)]
)

# Knob ref: from 1 to 10
knobs["max_background_flushes"] = {}
knobs["max_background_flushes"]["parameter_default"] = -1  # old: 1
# knobs["max_background_flushes"]["parameter_type"] = "integer"
# knobs["max_background_flushes"]["values"] = [-1, 10]
knobs["max_background_flushes"]["parameter_type"] = "ordinal"
knobs["max_background_flushes"]["values"] = [-1]

# Knob ref: from 5 to 15
knobs["max_bytes_for_level_multiplier"] = {}
knobs["max_bytes_for_level_multiplier"]["parameter_default"] = 10
# knobs["max_bytes_for_level_multiplier"]["parameter_type"] = "integer"
# knobs["max_bytes_for_level_multiplier"]["values"] = [5, 15]
knobs["max_bytes_for_level_multiplier"]["parameter_type"] = "ordinal"
knobs["max_bytes_for_level_multiplier"]["values"] = [10]

# Knob ref: from 1 to 2^7
knobs["max_write_buffer_number"] = {}
knobs["max_write_buffer_number"]["parameter_default"] = 2
knobs["max_write_buffer_number"]["parameter_type"] = "ordinal"
# knobs["max_write_buffer_number"]["values"] = [2 ** x for x in range(0, 8)]
knobs["max_write_buffer_number"]["values"] = [2]

# Knob ref: from 1 to 2^5
knobs["min_write_buffer_number_to_merge"] = {}
knobs["min_write_buffer_number_to_merge"]["parameter_default"] = 1
knobs["min_write_buffer_number_to_merge"]["parameter_type"] = "ordinal"
# knobs["min_write_buffer_number_to_merge"]["values"] = [2 ** x for x in range(0, 6)]
knobs["min_write_buffer_number_to_merge"]["values"] = [1]

# Knob ref: from 1 to 15*10^7
knobs["write_buffer_size"] = {}
knobs["write_buffer_size"]["parameter_default"] = 2 ** 26
knobs["write_buffer_size"]["parameter_type"] = "ordinal"
knobs["write_buffer_size"]["values"] = [2 ** 0] + [2 ** x for x in range(2, 31, 1)]
