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
CYPHER_DIR = "/home/osama/ldbc/ldbc_snb_interactive/cypher/"
DB_DIR = CYPHER_DIR + "scratch"
CONFIGURATION_FILE = CYPHER_DIR + "scratch/conf/neo4j.conf"
TEMPLATE_FILE = ROOT +"/util/neo4j_template2.conf"

##########################################################
#                     Tuning knobs                       #
##########################################################
knobs = {}

# T203, default: use memrec command in docker container to find out for the machine that is being used
knobs["dbms.memory.heap.max_size"] = {}
knobs["dbms.memory.heap.max_size"]["parameter_default"] = 5000
knobs["dbms.memory.heap.max_size"]["parameter_type"] = "ordinal"
knobs["dbms.memory.heap.max_size"]["values"] = [5000] + [x for x in range(int(5000/10), 5000*2, 1000)]
knobs["dbms.memory.heap.max_size"]["unit"] = "m"


# T211, default: use memrec. Default is 50% of the RAM available.
knobs["dbms.memory.pagecache.size"] = {}
knobs["dbms.memory.pagecache.size"]["parameter_default"] = 6400
knobs["dbms.memory.pagecache.size"]["parameter_type"] = "ordinal"
knobs["dbms.memory.pagecache.size"]["values"] = [6400] + [x for x in range(int(6400/10), 6400*2, 1000)]
knobs["dbms.memory.pagecache.size"]["unit"] = "m"


# T206, probably need to set dbms.tx_state.memory_allocation=OFF_HEAP, default 2.00GiB
knobs["dbms.memory.off_heap.max_size"] = {}
knobs["dbms.memory.off_heap.max_size"]["parameter_default"] = 2.00
knobs["dbms.memory.off_heap.max_size"]["parameter_type"] = "ordinal"
knobs["dbms.memory.off_heap.max_size"]["values"] = [x/10 for x in range(5, 50, 5)]
knobs["dbms.memory.off_heap.max_size"]["unit"] = "GiB"

# T302: Defines whether memory for transaction state should be allocated on- or off-heap
knobs["dbms.tx_state.memory_allocation"] = {}
knobs["dbms.tx_state.memory_allocation"]["parameter_default"] = "OFF_HEAP"
knobs["dbms.tx_state.memory_allocation"]["parameter_type"] = "categorical"
knobs["dbms.tx_state.memory_allocation"]["values"] = ["ON_HEAP", "OFF_HEAP"]


# T99-100, used if have a PERIODIC checkpoint in T98, default: [time: 15m, tx: 100000]
knobs["dbms.checkpoint.interval.time"] = {}
knobs["dbms.checkpoint.interval.time"]["parameter_default"] = 15
knobs["dbms.checkpoint.interval.time"]["parameter_type"] = "integer"
knobs["dbms.checkpoint.interval.time"]["values"] = [5, 25]
knobs["dbms.checkpoint.interval.time"]["unit"] = "m"

knobs["dbms.checkpoint.interval.tx"] = {}
knobs["dbms.checkpoint.interval.tx"]["parameter_default"] = 100000
knobs["dbms.checkpoint.interval.tx"]["parameter_type"] = "ordinal"
knobs["dbms.checkpoint.interval.tx"]["values"] = [
    x * 1000 for x in range(10, 200, 10)
]


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
knobs["dbms.memory.pagecache.flush.buffer.size_in_pages"]["parameter_type"] = "ordinal"
knobs["dbms.memory.pagecache.flush.buffer.size_in_pages"]["values"] = [2**x for x in range(0, 10)]
