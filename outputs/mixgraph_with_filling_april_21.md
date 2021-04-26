# Testing 50M key-value pairs with filling  

Benchmark with knobs: {}  
Throughput (ops/sec): 1411  
Average (ops/sec): **1411**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '16'}  
Throughput (ops/sec): 1439  
Average (ops/sec): **1439**  
Deviation from baseline: **1.98%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 1532  
Average (ops/sec): **1532**  
Deviation from baseline: **8.58%**  

Benchmark with knobs: {'write_buffer_size': '256'}  
Throughput (ops/sec): TIMEOUT --> very low ops/sec.  

Benchmark with knobs: {}  
Throughput (ops/sec): 1443  
Average (ops/sec): **1443**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '16'}  
Throughput (ops/sec): 1432  
Average (ops/sec): **1432**  
Deviation from baseline: **-0.76%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 1460  
Average (ops/sec): **1460**  
Deviation from baseline: **1.18%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 1439  
Average (ops/sec): **1439**  
Deviation from baseline: **-0.28%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 1476  
Average (ops/sec): **1476**  
Deviation from baseline: **2.29%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 1341  
Average (ops/sec): **1341**  
Deviation from baseline: **-7.07%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '12'}  
Throughput (ops/sec): 1414  
Average (ops/sec): **1414**  
Deviation from baseline: **-2.01%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '24'}  
Throughput (ops/sec): 1445  
Average (ops/sec): **1445**  
Deviation from baseline: **0.14%**  

## 1M keys

Benchmark with knobs: {}  
Throughput (ops/sec): 93076  
Average (ops/sec): **93076**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 94020  
Average (ops/sec): **94020**  
Deviation from baseline: **1.01%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 94184  
Average (ops/sec): **94184**  
Deviation from baseline: **1.19%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '12'}  
Throughput (ops/sec): 94603  
Average (ops/sec): **94603**  
Deviation from baseline: **1.64%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '24'}  
Throughput (ops/sec): 96445  
Average (ops/sec): **96445**  
Deviation from baseline: **3.62%**  

sudo /home/osama_eldawebi/main/rocksdb/db_bench --benchmarks="fillrandom" -num=50000000 -perf_level=3 -use_direct_io_for_flush_and_compaction=true -use_direct_reads=true -cache_size=268435456 -key_size=48 -value_size=43

sudo /home/osama_eldawebi/main/rocksdb/db_bench --benchmarks="mixgraph" --use_existing_db -use_direct_io_for_flush_and_compaction=true -use_direct_reads=true -cache_size=268435456 -keyrange_dist_a=14.18 -keyrange_dist_b=-2.917 -keyrange_dist_c=0.0164 -keyrange_dist_d=-0.08082 -keyrange_num=30 -value_k=0.2615 -value_sigma=25.45 -iter_k=2.517 -iter_sigma=14.236 -mix_get_ratio=0.85 -mix_put_ratio=0.14 -mix_seek_ratio=0.01 -sine_mix_rate_interval_milliseconds=5000 -sine_a=100000 -sine_b=0.073 -sine_d=4500 --perf_level=2 -reads=420000000 -num=50000000 -key_size=48