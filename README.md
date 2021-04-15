# Database tuning project
Running `config.py` and `setup_optimizer_config.py` will create the the json files that are needed. Then afterwards the optimizer should be run using `run_optimizer.py`.

I used an Anaconda environment with Python3.8. 

The dependencies are in the *requirements.txt* file. To replicate the environment, you can just run:

```conda create --name <envname> --file requirements.txt```

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

# Mixgraph tests with no fills
Benchmark with the following knowb configurations: {} \
Throughput (ops/sec): 87044 \
Throughput (ops/sec): 87063 \
Throughput (ops/sec): 86664 \
Benchmark with the following knowb configurations: {'max_background_compactions': '8', 'compaction_readahead_size': '500000'} \
Throughput (ops/sec): 86689 \
Throughput (ops/sec): 86526 \
Throughput (ops/sec): 86194 \
Benchmark with the following knowb configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '2000000'} \
Throughput (ops/sec): 86380 \
Throughput (ops/sec): 86228 \
Throughput (ops/sec): 86425 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'level0_slowdown_writes_trigger': '256', 'write_buffer_size': '256'} \
Throughput (ops/sec): 86343 \
Throughput (ops/sec): 86232 \
Throughput (ops/sec): 86092 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'level0_slowdown_writes_trigger': '1024', 'write_buffer_size': '268435456'} \
Throughput (ops/sec): 86368 \
Throughput (ops/sec): 86672 \
Throughput (ops/sec): 86654 \
Benchmark with the following knob configurations: {'max_background_compactions': '8', 'block_size': '64'} \
Throughput (ops/sec): 86736 \
Throughput (ops/sec): 86295 \
Throughput (ops/sec): 86551 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'block_size': '65536'} \
Throughput (ops/sec): 86894 \
Throughput (ops/sec): 86777 \
Throughput (ops/sec): 85939 \
Benchmark with the following knob configurations: {'max_background_compactions': '64', 'compaction_readahead_size': '500000', 'level0_slowdown_writes_trigger': '24', 'write_buffer_size': '256', 'optimize_filters_for_hits': 'True', 'block_size': '64'} \
Throughput (ops/sec): 86806 \
Throughput (ops/sec): 86943 \
Throughput (ops/sec): 87350

## YCSB
A:
Throughput (ops/sec): 3891.0505836575876
Throughput (ops/sec): 3521.1267605633802
Throughput (ops/sec): 3921.5686274509803
B:
Throughput (ops/sec): 4347.826086956522
Throughput (ops/sec): 4504.504504504504
Throughput (ops/sec): 4629.62962962963
C:
Throughput (ops/sec): 4149.377593360996
Throughput (ops/sec): 4132.231404958678
Throughput (ops/sec): 4830.917874396136

Values for YCSB look odd because they are very low. Found out via https://github.com/brianfrankcooper/YCSB/wiki/Running-a-Workload#step-5-load-the-data that the standard workloads actually create very small databases. "workloada (A) creates only 1,000 records".

Following the steps in the link, we should we able to configure to size of the benchmarking data quite easily.