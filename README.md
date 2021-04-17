# Database tuning project
Running `config.py` and `setup_optimizer_config.py` will create the the json files that are needed. Then afterwards the optimizer should be run using `run_optimizer.py`.

I used an Anaconda environment with Python3.8. 

The dependencies are in the *requirements.txt* file. To replicate the environment, you can just run:

```conda create --name <envname> --file requirements.txt```

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

## OLD YCSB pure testing, not changing any knobs  
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