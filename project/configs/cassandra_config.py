"""
Configuration file for Cassandra optimizer parameters and tuning knobs.
"""
import os
import numpy as np

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
SNAPSHOT_TABLE = "usertable-f96dcfc06a6411ec889309821810ed4f"
DB_DIR = "/var/lib/cassandra/data/"
DB_COMMITLOGS_DIR = "/var/lib/cassandra/commitlog/"
BACKUP_DIR = "/home/ubuntu/backup_data/"
BACKUP_COMMITLOGS_DIR = "/home/ubuntu/backup_commitlogs/"

CONFIGURATION_FILE_TEMPLATE = ROOT + "/util/cassandra_default_snic.yaml"
CONFIGURATION_FILE_TARGET = "/etc/cassandra/cassandra.yaml"

YCSB_PATH = f"{ROOT}/../ycsb-0.17.0/"
YCSB_WORKLOAD_FILE = YCSB_PATH + "workloads/workloadc"
YCSB_OUTPUT_FILE = YCSB_PATH + "outputRun.txt"
YCSB_LOAD_OUTPUT_FILE = YCSB_PATH + "outputLoad.txt"

##########################################################
#                     Tuning knobs                       #
##########################################################
knobs = {}

# Silva-Munoz et al. 2021

knobs["compaction_method"] = {}
knobs["compaction_method"]["parameter_default"] = ""
knobs["compaction_method"]["parameter_type"] = "categorical"
knobs["compaction_method"]["values"] = ["", "Leveled", "SizeTiered"]

knobs["compaction_throughput_mb_per_sec"] = {}
knobs["compaction_throughput_mb_per_sec"]["parameter_default"] = 16
knobs["compaction_throughput_mb_per_sec"]["parameter_type"] = "ordinal"
knobs["compaction_throughput_mb_per_sec"]["values"] = [2 ** x for x in range(4, 7)]

knobs["concurrent_compactors"] = {}
knobs["concurrent_compactors"]["parameter_default"] = 4  # number of cores
knobs["concurrent_compactors"]["parameter_type"] = "integer"
knobs["concurrent_compactors"]["values"] = [2, 16]

knobs["concurrent_reads"] = {}
knobs["concurrent_reads"]["parameter_default"] = 32
knobs["concurrent_reads"]["parameter_type"] = "integer"
knobs["concurrent_reads"]["values"] = [8, 64]

knobs["concurrent_writes"] = {}
knobs["concurrent_writes"]["parameter_default"] = 32
knobs["concurrent_writes"]["parameter_type"] = "integer"
knobs["concurrent_writes"]["values"] = [8, 64]

knobs["file_cache_size_in_mb"] = {}
knobs["file_cache_size_in_mb"][
    "parameter_default"
] = 512  # min(1/4 of heap, 512) actually
knobs["file_cache_size_in_mb"]["parameter_type"] = "ordinal"
knobs["file_cache_size_in_mb"]["values"] = [2 ** x for x in range(8, 12)]

knobs["memtable_heap_space_in_mb"] = {}
knobs["memtable_heap_space_in_mb"]["parameter_default"] = 2048  # approx 1/4 of RAM
knobs["memtable_heap_space_in_mb"]["parameter_type"] = "ordinal"
knobs["memtable_heap_space_in_mb"]["values"] = np.linspace(
    1024, 4096, 10, dtype=np.int16
).tolist()

knobs["memtable_offheap_space_in_mb"] = {}
knobs["memtable_offheap_space_in_mb"]["parameter_default"] = 2048  # approx 1/4 of RAM
knobs["memtable_offheap_space_in_mb"]["parameter_type"] = "ordinal"
knobs["memtable_offheap_space_in_mb"]["values"] = np.linspace(
    1024, 4096, 10, dtype=np.int16
).tolist()

knobs["memtable_allocation_type"] = {}
knobs["memtable_allocation_type"][
    "parameter_default"
] = "heap_buffers"  # approx 1/4 of RAM
knobs["memtable_allocation_type"]["parameter_type"] = "categorical"
knobs["memtable_allocation_type"]["values"] = [
    "heap_buffers",
    "offheap_buffers",
    "offheap_objects",
]

knobs["row_cache_size_in_mb"] = {}
knobs["row_cache_size_in_mb"]["parameter_default"] = 0  # disabled by default
knobs["row_cache_size_in_mb"]["parameter_type"] = "integer"
knobs["row_cache_size_in_mb"]["values"] = [0, 16]

knobs["sstable_preemptive_open_interval_in_mb"] = {}
knobs["sstable_preemptive_open_interval_in_mb"]["parameter_default"] = 50
knobs["sstable_preemptive_open_interval_in_mb"]["parameter_type"] = "ordinal"
knobs["sstable_preemptive_open_interval_in_mb"]["values"] = np.linspace(
    0, 100, 11, dtype=np.int16
).tolist()
