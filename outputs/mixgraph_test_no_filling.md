# Mixgraph tests with no fills  

Benchmark with the following knob configurations: {}  
Throughput (ops/sec): 85878  
Throughput (ops/sec): 84950  
Throughput (ops/sec): 85567  
Average (ops/sec): **85465**  
Deviation from baseline: **0.00%**

Benchmark with the following knob configurations: {'max_background_compactions': '8'}  
Throughput (ops/sec): 85654  
Throughput (ops/sec): 85338**  
Throughput (ops/sec): 85510  
Average (ops/sec): **85500**  
Deviation from baseline: **0.04%**  

Benchmark with the following knob configurations: {'max_background_compactions': '32'}  
Throughput (ops/sec): 85537  
Throughput (ops/sec): 85841  
Throughput (ops/sec): 85767  
Average (ops/sec): **85715**  
Deviation from baseline: **0.30%**  

Benchmark with the following knob configurations: {'max_background_compactions': '64'}  
Throughput (ops/sec): 85703  
Throughput (ops/sec): 85674  
Throughput (ops/sec): 85519   
Average (ops/sec): **85632**  
Deviation from baseline: **0.20%**  

Benchmark with the following knob configurations: {'write_buffer_size': '256'}  
Throughput (ops/sec): 85499  
Throughput (ops/sec): 85732  
Throughput (ops/sec): 85697  
Average (ops/sec): **85642**  
Deviation from baseline: **0.21%**   

Benchmark with the following knob configurations: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 85545  
Throughput (ops/sec): 85723  
Throughput (ops/sec): 85832  
Average (ops/sec): **85700**  
Deviation from baseline: **0.27%**  

Benchmark with the following knob configurations: {'block_size': '4'}  
Throughput (ops/sec): 85772  
Throughput (ops/sec): 85293  
Throughput (ops/sec): 85269  
Average (ops/sec): **85444**  
Deviation from baseline: **-0.02%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 84759  
Throughput (ops/sec): 85133  
Throughput (ops/sec): 85422  
Average (ops/sec): **85104**  
Deviation from baseline: **-0.42%**  

## After upgrading SSD from 50 GB to 150 GB  

Benchmark with knobs: {}  
Throughput (ops/sec): 83450  
Throughput (ops/sec): 82133  
Throughput (ops/sec): 83246  
Average (ops/sec): **82943**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '8'}  
Throughput (ops/sec): 83288  
Throughput (ops/sec): 82103  
Throughput (ops/sec): 82656  
Average (ops/sec): **82682**  
Deviation from baseline: **-0.31%**  

Benchmark with knobs: {'max_background_compactions': '32'}  
Throughput (ops/sec): 82590  
Throughput (ops/sec): 82378  
Throughput (ops/sec): 83405  
Average (ops/sec): **82791**  
Deviation from baseline: **-0.18%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 82749  
Throughput (ops/sec): 81371  
Throughput (ops/sec): 83166  
Average (ops/sec): **82428**  
Deviation from baseline: **-0.62%**  

Benchmark with knobs: {'write_buffer_size': '256'}  
Throughput (ops/sec): 82933  
Throughput (ops/sec): 82848  
Throughput (ops/sec): 79507  
Average (ops/sec): **81762**  
Deviation from baseline: **-1.42%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 81484  
Throughput (ops/sec): 81423  
Throughput (ops/sec): 83165  
Average (ops/sec): **82024**  
Deviation from baseline: **-1.11%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 80592  
Throughput (ops/sec): 82127  
Throughput (ops/sec): 82523  
Average (ops/sec): **81747**  
Deviation from baseline: **-1.44%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 82289  
Throughput (ops/sec): 82683  
Throughput (ops/sec): 81819  
Average (ops/sec): **82263**  
Deviation from baseline: **-0.82%**  

Benchmark with knobs: {}  
Throughput (ops/sec): 85534  

Benchmark with knobs: {}  
Throughput (ops/sec): 105222  

# Threads = 4
Benchmark with knobs: {}  
Throughput (ops/sec): 106188  
Throughput (ops/sec): 106342  