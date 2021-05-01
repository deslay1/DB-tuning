## Readrandom test with 5M keys with loading before every benchmark run

Benchmark with knobs: {}  
Throughput (ops/sec): 181051  
Throughput (ops/sec): 181034  
Throughput (ops/sec): 182335  
Average (ops/sec): **181473**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 177379  
Throughput (ops/sec): 179108  
Throughput (ops/sec): 176330  
Average (ops/sec): **177605**  
Deviation from baseline: **-2.13%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8'}  
Throughput (ops/sec): 29085  
Throughput (ops/sec): 29511  
Throughput (ops/sec): 29162  
Average (ops/sec): **29252**  
Deviation from baseline: **-83.88%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8', 'write_buffer_size': '268435456'}  
Throughput (ops/sec): 29355  
Throughput (ops/sec): 28941  
Throughput (ops/sec): 29782  
Average (ops/sec): **29359**  
Deviation from baseline: **-83.82%**  

## same as above but with "readwhilewriting"
Benchmark with knobs: {}  
Throughput (ops/sec): 64545  
Throughput (ops/sec): 65475  
Throughput (ops/sec): 66592  
Average (ops/sec): **65537**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 67172  
Throughput (ops/sec): 67811  
Throughput (ops/sec): 66944  
Average (ops/sec): **67309**  
Deviation from baseline: **2.70%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8'}  
Throughput (ops/sec): 56496  


## readrandom again, but with singular knob changes  

Benchmark with knobs: {}  
Throughput (ops/sec): 182023  
Throughput (ops/sec): 181937  
Throughput (ops/sec): 181401  
Average (ops/sec): **181787**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'write_buffer_size': '262144'}  
Throughput (ops/sec): 179870  
Throughput (ops/sec): 179381  
Throughput (ops/sec): 178364  
Average (ops/sec): **179205**  
Deviation from baseline: **-1.42%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 184170  
Throughput (ops/sec): 186368  
Throughput (ops/sec): 183641  
Average (ops/sec): **184726**  
Deviation from baseline: **1.62%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 193578  
Throughput (ops/sec): 193370  
Throughput (ops/sec): 195622  
Average (ops/sec): **194190**  
Deviation from baseline: **6.82%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 9634  
Throughput (ops/sec): 9706  
Throughput (ops/sec): 9794  
Average (ops/sec): **9711**  
Deviation from baseline: **-94.66%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '8'}  
Throughput (ops/sec): 179549  
Throughput (ops/sec): 183433  
Throughput (ops/sec): 182586  
Average (ops/sec): **181856**  
Deviation from baseline: **0.04%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '24'}  
Throughput (ops/sec): 174771  
Throughput (ops/sec): 182117  
Throughput (ops/sec): 182881  
Average (ops/sec): **179923**  
Deviation from baseline: **-1.03%**  

## Readrandom with 10M keys

Benchmark with knobs: {}  
Throughput (ops/sec): 178727  
Throughput (ops/sec): 179072  
Throughput (ops/sec): 177042  
Average (ops/sec): **178280**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 173262  
Throughput (ops/sec): 170752  
Throughput (ops/sec): 174770  
Average (ops/sec): **172928**  
Deviation from baseline: **-3.00%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8'}  
Throughput (ops/sec): 26759  
Throughput (ops/sec): 26842  
Throughput (ops/sec): 27556  
Average (ops/sec): **27052**  
Deviation from baseline: **-84.83%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8', 'write_buffer_size': '268435456'}  
Throughput (ops/sec): 26851  
Throughput (ops/sec): 26644  
Throughput (ops/sec): 27247  
Average (ops/sec): **26914**  
Deviation from baseline: **-84.90%**  

Benchmark with knobs: {'write_buffer_size': '262144'}  
Throughput (ops/sec): 169405  
Throughput (ops/sec): 168498  
Throughput (ops/sec): 165113  
Average (ops/sec): **167672**  
Deviation from baseline: **-5.95%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 168657  
Throughput (ops/sec): 174699  
Throughput (ops/sec): 171137  
Average (ops/sec): **171497**  
Deviation from baseline: **-3.80%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 171649  
Throughput (ops/sec): 169149  
Throughput (ops/sec): 167515  
Average (ops/sec): **169437**  
Deviation from baseline: **-4.96%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 9531  
Throughput (ops/sec): 9136  
Throughput (ops/sec): 9421  
Average (ops/sec): **9362**  
Deviation from baseline: **-94.75%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '8'}  
Throughput (ops/sec): 166574  
Throughput (ops/sec): 165513  
Throughput (ops/sec): 166989  
Average (ops/sec): **166358**  
Deviation from baseline: **-6.69%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '24'}  
Throughput (ops/sec): 169115  
Throughput (ops/sec): 170413  
Throughput (ops/sec): 168318  
Average (ops/sec): **169282**  
Deviation from baseline: **-5.05%**  

## Readrandom with 50M keys

Benchmark with knobs: {}  
Throughput (ops/sec): 157541  
Throughput (ops/sec): 150607  
Throughput (ops/sec): 149748  
Average (ops/sec): **152632**  
Deviation from baseline: **0.00%**  

Benchmark with knobs: {'max_background_compactions': '64'}  
Throughput (ops/sec): 148289  
Throughput (ops/sec): 156894  
Throughput (ops/sec): 154493  
Average (ops/sec): **153225**  
Deviation from baseline: **0.39%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8'}  
Throughput (ops/sec): 29324  
Throughput (ops/sec): 29701  
Throughput (ops/sec): 29306  
Average (ops/sec): **29443**  
Deviation from baseline: **-80.71%**  

Benchmark with knobs: {'max_background_compactions': '64', 'level0_file_num_compaction_trigger': '8', 'write_buffer_size': '268435456'}  
Throughput (ops/sec): 29081  
Throughput (ops/sec): 28456  
Throughput (ops/sec): 28802  
Average (ops/sec): **28779**  
Deviation from baseline: **-81.14%**  

Benchmark with knobs: {'write_buffer_size': '262144'}  
Throughput (ops/sec): 151838  
Throughput (ops/sec): 151459  
Throughput (ops/sec): 151981  
Average (ops/sec): **151759**  
Deviation from baseline: **-0.57%**  

Benchmark with knobs: {'write_buffer_size': '268435456'}  
Throughput (ops/sec): 153662  
Throughput (ops/sec): 151251  
Throughput (ops/sec): 154377  
Average (ops/sec): **153096**  
Deviation from baseline: **0.30%**  

Benchmark with knobs: {'block_size': '4'}  
Throughput (ops/sec): 120298  
Throughput (ops/sec): 123197  
Throughput (ops/sec): 122746  
Average (ops/sec): **122080**  
Deviation from baseline: **-20.02%**  

Benchmark with knobs: {'block_size': '262144'}  
Throughput (ops/sec): 8847  
Throughput (ops/sec): 8818  
Throughput (ops/sec): 9441  
Average (ops/sec): **9035**  
Deviation from baseline: **-94.08%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '8'}  
Throughput (ops/sec): 149364  
Throughput (ops/sec): 159864  
Throughput (ops/sec): 156994  
Average (ops/sec): **155407**  
Deviation from baseline: **1.82%**  

Benchmark with knobs: {'level0_slowdown_writes_trigger': '24'}  
Throughput (ops/sec): 153377  
Throughput (ops/sec): 152070  
Throughput (ops/sec): 155629  
Average (ops/sec): **153692**  
Deviation from baseline: **0.69%**  