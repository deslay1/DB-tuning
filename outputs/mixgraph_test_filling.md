# Mixgraph tests with pre-filling

## Amount filled in database: 50 million
Benchmark with the following knob configurations: {} \
Throughput (ops/sec): 931 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'compaction_readahead_size': '500000'} \
Throughput (ops/sec): 1002 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '2000000'} \
Throughput (ops/sec): 1427 \
--> Reasonable! max_background_compactions is actually very important. \
 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'block_size': '65536'} \
Throughput (ops/sec): 1421 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'compaction_readahead_size': '500000', 'optimize_filters_for_hits': 'True', 'block_size': '16000'} \
Throughput (ops/sec): 915 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '2000000', 'level0_slowdown_writes_trigger': '24', 'optimize_filters_for_hits': 'True', 'block_size': '16000'} \
Throughput (ops/sec): 1343 \
Benchmark with the following knob configurations: {} \
Throughput (ops/sec): 955 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '2000000', 'level0_slowdown_writes_trigger': '24', 'level0_stop_writes_trigger': '40', 'optimize_filters_for_hits': 'True', 'block_size': '16000'} \
Throughput (ops/sec): 1342 \
--> Not so good tests, but perhaps illustrates that I shouldn't use to many knobs from the beginning.

Benchmark with the following knob configurations: {'max_background_compactions': '64', 'block_size': '64'} \
Throughput (ops/sec): 1401 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'block_size': '65536'} \
Throughput (ops/sec): 1389 \
-- Lower block_size leading to better ops is perhaps reasonable.

## Amount filled in database: 1 million
Benchmark with the following knob configurations: {} \
Throughput (ops/sec): 70090 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '2000000', 'level0_slowdown_writes_trigger': '24', 'level0_stop_writes_trigger': '40', 'optimize_filters_for_hits': 'True', 'block_size': '16000'} \
Throughput (ops/sec): 28088 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'compaction_readahead_size': '10000'} \
Throughput (ops/sec): 71464 \
Benchmark with the following knob configurations: {'max_background_compactions': '32', 'compaction_readahead_size': '500000'} \
Throughput (ops/sec): 27807 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '2000000'} \
Throughput (ops/sec): 28709

### --> Is max_background_compactions the problem or compaction_readahead_size?
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '10000'} \
Throughput (ops/sec): 70305 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'compaction_readahead_size': '2000000'} \
Throughput (ops/sec): 27907 \
--> compaction_readahead_size is the problem 

### What if filled the database with keys in sequential order instead of random? 
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '10000'} \
Throughput (ops/sec): 69515 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'compaction_readahead_size': '2000000'} \
Throughput (ops/sec): 28521 \
--> Almost no difference