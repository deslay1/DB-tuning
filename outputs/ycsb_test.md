# YCSB Tests

### Proportions
readproportion=0.85  
updateproportion=0.10  
insertproportion=0.05  

## Using only 5000 records and operations

Benchmark with knobs: {}  
Throughput (ops/sec): 29585.798816568047  
Throughput (ops/sec): 34364.26116838488  
Throughput (ops/sec): 36603.22108345534  
Average (ops/sec): **33517**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '8'}  
Throughput (ops/sec): 29568.30277942046  
Throughput (ops/sec): 34317.08991077557  
Throughput (ops/sec): 32851.5111695138  
Average (ops/sec): **32245**  
Deviation from baseline: **-3.80%**  

Benchmark with knobs: {'max_background_compactions': '32'}  
Throughput (ops/sec): 28153.153153153155  
Throughput (ops/sec): 35410.76487252125  
Throughput (ops/sec): 36075.03607503608  
Average (ops/sec): **33212**  
Deviation from baseline: **-0.91%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 27995.52071668533  
Throughput (ops/sec): 36496.3503649635  
Throughput (ops/sec): 36549.70760233918  
Average (ops/sec): **33680**  
Deviation from baseline: **0.49%**  

Benchmark with knobs: {'write_buffer_size': '256'}  
Throughput (ops/sec): 28785.261945883707  
Throughput (ops/sec): 35816.61891117479  
Throughput (ops/sec): 34506.55624568668  
Average (ops/sec): **33036**  
Deviation from baseline: **-1.44%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 28264.55624646693  
Throughput (ops/sec): 34794.71120389701  
Throughput (ops/sec): 34867.50348675035  
Average (ops/sec): **32642**  
Deviation from baseline: **-2.61%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 20859.407592824366  
Throughput (ops/sec): 31036.623215394164  
Throughput (ops/sec): 34674.06380027739  
Average (ops/sec): **28856**  
Deviation from baseline: **-13.91%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 20234.722784297854  
Throughput (ops/sec): 32278.889606197547  
Throughput (ops/sec): 33806.62609871535  
Average (ops/sec): **28773**  
Deviation from baseline: **-14.15%**  

## Using 50M records and operations  
This is not a good test. For my setup, testing a single configuration would take multiple hours, perhaps half a day. For many configurations and multiple returns to calculate average, we are talking about weeks of testing. It also uses 50 GB.