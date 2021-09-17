"""
Configuration file for Neo4j optimizer parameters and tuning knobs.
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
CYPHER_DIR = "/home/ubuntu//ldbc/ldbc_snb_interactive/cypher/"
DB_DIR = CYPHER_DIR + "scratch"
CONFIGURATION_FILE = CYPHER_DIR + "scratch/conf/neo4j.conf"

##########################################################
#                     Tuning knobs                       #
##########################################################
knobs = {}

# T203, default: 3.7(?)
knobs["dbms.memory.heap.max_size"] = {}
knobs["dbms.memory.heap.max_size"]["parameter_default"] = 3.7
knobs["dbms.memory.heap.max_size"]["parameter_type"] = "ordinal"
knobs["dbms.memory.heap.max_size"]["values"] = [x / 1000 for x in range(100, 6000, 250)]
knobs["dbms.memory.heap.max_size"]["unit"] = "GB"


# T211, default: 512M(?). Default is 50% of the RAM available.
knobs["dbms.memory.pagecache.size"] = {}
knobs["dbms.memory.pagecache.size"]["parameter_default"] = 512
knobs["dbms.memory.pagecache.size"]["parameter_type"] = "ordinal"
knobs["dbms.memory.pagecache.size"]["values"] = sorted(
    [512] + [x / 1000 for x in range(50, 2000, 200)]
)
knobs["dbms.memory.heap.max_size"]["unit"] = "M"


# T206, probably need to set dbms.tx_state.memory_allocation=OFF_HEAP, default 2.00GiB
knobs["dbms.memory.off_heap.max_size"] = {}
knobs["dbms.memory.off_heap.max_size"]["parameter_default"] = 0
knobs["dbms.memory.off_heap.max_size"]["parameter_type"] = "ordinal"
knobs["dbms.memory.off_heap.max_size"]["values"] = [x for x in range(100, 1000, 100)]
knobs["dbms.memory.off_heap.max_size"]["unit"] = "GiB"


# T99-100, used if have a PERIODIC checkpoint in T98, default: [time: 15m, tx: 100000]
knobs["dbms.checkpoint.interval.time"] = {}
knobs["dbms.checkpoint.interval.time"]["parameter_default"] = 15
knobs["dbms.checkpoint.interval.time"]["parameter_type"] = "integer"
knobs["dbms.checkpoint.interval.time"]["values"] = [5, 25]
knobs["dbms.checkpoint.interval.time"]["unit"] = "m"

knobs["dbms.checkpoint.interval.time"] = {}
knobs["dbms.checkpoint.interval.time"]["parameter_default"] = 100000
knobs["dbms.checkpoint.interval.time"]["parameter_type"] = "ordinal"
knobs["dbms.checkpoint.interval.time"]["values"] = [
    x * 1000 for x in range(10, 200, 10)
]
knobs["dbms.checkpoint.interval.time"]["unit"] = "m"


# T153, e.g. -XX:+UseCompressedOops (incl in https://neo4j.com/docs/operations-manual/current/performance/gc-tuning/#gc-tuning),
#            -XX:ParallelGCThreads=n, -XX:+OptimizeStringConcat, -XX:+UseStringCache from https://www.oracle.com/java/technologies/javase/vmoptions-jsp.html#PerformanceTuning
# default is empty(?)
knobs["dbms.jvm.additional"] = {}
knobs["dbms.jvm.additional"]["parameter_default"] = ""
knobs["dbms.jvm.additional"]["parameter_type"] = "categorical"
knobs["dbms.jvm.additional"]["values"] = [
    "",
    "-XX:+UseCompressedOops",
    "-XX:+OptimizeStringConcat",
    "-XX:+UseStringCache ",
]


# T208-209, default: [ buffer-enabled: false, buffer-size: 128 (1-512) ]
knobs["dbms.memory.pagecache.flush.buffer.enabled"] = {}
knobs["dbms.memory.pagecache.flush.buffer.enabled"]["parameter_default"] = "false"
knobs["dbms.memory.pagecache.flush.buffer.enabled"]["parameter_type"] = "categorical"
knobs["dbms.memory.pagecache.flush.buffer.enabled"]["values"] = ["false", "true"]

knobs["dbms.memory.pagecache.flush.buffer.size_in_pages"] = {}
knobs["dbms.memory.pagecache.flush.buffer.size_in_pages"]["parameter_default"] = 16
knobs["dbms.memory.pagecache.flush.buffer.size_in_pages"]["parameter_type"] = "integer"
knobs["dbms.memory.pagecache.flush.buffer.size_in_pages"]["values"] = [10, 20]