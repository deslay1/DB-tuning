"""
Configuration file for Cassandra optimizer parameters and tuning knobs.
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
DB_DIR = "/var/lib/cassandra/data/"

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

knobs["concurrent_compactors"] = {}
knobs["concurrent_compactors"]["parameter_default"] = 4  # number of cores
knobs["concurrent_compactors"]["parameter_type"] = "integer"
knobs["concurrent_compactors"]["values"] = [2, 16]

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
