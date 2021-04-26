## Mixgraph no filling with updated --duration flag

Benchmark with knobs: {}  
Throughput (ops/sec): 70982  
Throughput (ops/sec): 71461  
Throughput (ops/sec): 69575  
Average (ops/sec): **70672**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 70058  
Throughput (ops/sec): 69580  
Throughput (ops/sec): 71049  
Average (ops/sec): **70229**  
Deviation from baseline: **-0.63%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8'}  
Throughput (ops/sec): 71067  
Throughput (ops/sec): 71105  
Throughput (ops/sec): 69757  
Average (ops/sec): **70643**  
Deviation from baseline: **-0.04%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8', 'write_buffer_size': '8388608'}  
Throughput (ops/sec): 49418  
Throughput (ops/sec): 48646  
Throughput (ops/sec): 49501  
Average (ops/sec): **49188**  
Deviation from baseline: **-30.40%**  

ABOVE REPEATED FOR SANITY CHECK:
Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8', 'write_buffer_size': '8388608'}  
Throughput (ops/sec): 44485  
Throughput (ops/sec): 41775  
Throughput (ops/sec): 43687  
Average (ops/sec): **43315**  
Deviation from baseline: **-38.32%**  

WRITE BUFFER SIZE NOW LARGER THAN DEFAULT (in the above it is smaller):
Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8', 'write_buffer_size': '268435456'}  
Throughput (ops/sec): 90539  
Throughput (ops/sec): 94365  
Throughput (ops/sec): 94941  
Average (ops/sec): **93281**  
Deviation from baseline: **32.82%**  