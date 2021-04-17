# Mixgraph tests with pre-filling

## Pre-fill with 1 M records and operations

Benchmark with knobs: {}  
Throughput (ops/sec): 53802  
Throughput (ops/sec): 54784  
Throughput (ops/sec): 54926  
Average (ops/sec): **54504**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '8'}  
Throughput (ops/sec): 55496  
Throughput (ops/sec): 55600  
Throughput (ops/sec): 55674  
Average (ops/sec): **55590**  
Deviation from baseline: **1.99%**   

Benchmark with knobs: {'max_background_compactions': '32'}  
Throughput (ops/sec): 55323  
Throughput (ops/sec): 55218  
Throughput (ops/sec): 55356  
Average (ops/sec): **55299**  
Deviation from baseline: **1.46%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 55545  
Throughput (ops/sec): 54744  
Throughput (ops/sec): 54532  
Average (ops/sec): **54940**  
Deviation from baseline: **0.80%**  

Benchmark with knobs: {'write_buffer_size': '256'}  
Throughput (ops/sec): 55679  
Throughput (ops/sec): 55745  
Throughput (ops/sec): 55685  
Average (ops/sec): **55703**  
Deviation from baseline: **2.20%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 46744  
Throughput (ops/sec): 45921  
Throughput (ops/sec): 46296  
Average (ops/sec): **46320**  
Deviation from baseline: **-15.02%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 46015  
Throughput (ops/sec): 46481  
Throughput (ops/sec): 48813  
Average (ops/sec): **47103**  
Deviation from baseline: **-13.58%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 46427  
Throughput (ops/sec): 46910  
Throughput (ops/sec): 47028  
Average (ops/sec): **46788**  
Deviation from baseline: **-14.16%**  

## Pre-fill with 50 M records and operations  

Benchmark with knobs: {}  
Throughput (ops/sec): 77858  
Throughput (ops/sec): 82873  
Throughput (ops/sec): 81898  
Average (ops/sec): **80876**  
Deviation from baseline: **0.00%**  

**All tests below have much lower throughput. I believe the above configuration test is incorrect and should match the number we see below.**

Benchmark with knobs: {'max_background_compactions': '16'}  
Throughput (ops/sec): 866  
Throughput (ops/sec): 895  
Throughput (ops/sec): 840  
Average (ops/sec): **867**  
Deviation from baseline: **-98.93%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 864  
Throughput (ops/sec): 954  
Throughput (ops/sec): 889  
Average (ops/sec): **902**  
Deviation from baseline: **-98.88%**  

Benchmark with knobs: {'write_buffer_size': '256'}  
Throughput (ops/sec): 921  
Throughput (ops/sec): 949  
Throughput (ops/sec): 938  
Average (ops/sec): **936**  
Deviation from baseline: **-98.84%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 864  
Throughput (ops/sec): 516  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '12'}  
Throughput (ops/sec): 884  
Average (ops/sec): **754**  
Deviation from baseline: **-99.07%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 917  
Throughput (ops/sec): 962  
Throughput (ops/sec): 925  
Average (ops/sec): **934**  
Deviation from baseline: **-98.85%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 939  
Throughput (ops/sec): 982  
Throughput (ops/sec): 950  
Average (ops/sec): **957**  
Deviation from baseline: **-98.82%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '12'}  
Throughput (ops/sec): 906  
Throughput (ops/sec): 917  
Throughput (ops/sec): 962  
Average (ops/sec): **928**  
Deviation from baseline: **-98.85%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '24'}  
Throughput (ops/sec): 927  
Throughput (ops/sec): 933  
Throughput (ops/sec): 922  
Average (ops/sec): **927**  
Deviation from baseline: **-98.85%**  