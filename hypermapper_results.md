# First iteration of results
global properties:
- number of samples before optimization: 2
- model: random forest
  - numer of trees: \<default:20\>
- iterations: 50
- threads: 32
- runs per iteration: 1
- key-value pairs (num): 5 million
- max duration of benchmark: 60 seconds
- OUTPUT FILES: \<benchmark\>50.csv; 
## readrandomwriterandom
**feature importances**:  
[0.055445107303136155, 0.048877700628293136, 0.01929532842262805, 0.13084902528584758, 0.023027046103120306, 0.02813681783435002, 0.021166692624159107, 0.009288342610501783, 0.00403001343594297, 0.00670673010188481, 0.6531771956501362]

**Best point found**:  
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
4,160000,1,1024,4,256,2,8,64,1,33554432,-119597

## updaterandom
**feature importances**: [0.15385905108085335, 0.008006894642432242, 0.00540808190366646, 0.000516770446485539, 0.0798487068106021, 0.03331838540360432, 0.003290172332434804, 0.03354940429782523, 0.03600661420363871, 0.008655696717949395, 0.6375402221605079]

**Best point found**:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
512,120000,2,64,512,256,1,6,8,32,536870912,-58958

## readrandom
**feature importances**: [0.3812921587681154, 0.024027374605416867, 0.11893936120198154, 0.0009652864466218999, 0.027704099012557624, 0.007727132095317659, 0.006051348600476096, 0.003353719444603654, 0.007245856209043429, 0.008801271384755359, 0.4138923922311105]

**Best point found**:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
1024,40000,4,128,8,4,4,8,1,2,536870912,-248288


## readrandomwriterandom replicating workloads A,B,C in YCSB
### A: see above, but another test was done:
**feature importances**:
[0.2427261065744868, 0.00872722484428371, 0.07871058636288579, 0.006044349328470506, 0.03823827186586416, 0.031168650836803775, 0.00567687162748982, 0.01761936242583223, 0.01636744173920168, 0.008792852777551355, 0.5459282816171303]

**Best point found**:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
1024,120000,1,8,4,4,3,0,1,1,16777216,-121801

### B: 95/5 read/write  
**feature importances**:
[0.20279484902992875, 0.007752543941133131, 0.2610904103793222, 0.1749630376948556, 0.009403681091173448, 0.015963922350249304, 0.008356108236070211, 0.0018887666516706496, 0.005043839904741455, 0.012920309336572813, 0.29982253138428255]

**Best point found**:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
2048,240000,4,16,256,2,4,5,4,8,268435456,-262537

### C: 100/0 read/write - INVALID


## mixgraph 5 million
number of reads is 4.2 million
- rest is similar to Alabed

**feature importances**:
[0.3407670474741084, 0.01706067975979753, 0.23038264182710874, 0.002729358980699036, 0.09511747315795435, 0.08210144795297077, 0.008928392789567386, 0.016076557274410964, 0.0031041338907908974, 0.0014384009909340766, 0.2022938659016579]

**Best point found**:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
8192,40000,1,1024,32,256,3,5,8,4,1073741824,-15226

### another try:
**feature importances**:
[0.2231962367872672, 0.0, 0.010535100772364086, 0.13473192973427256, 0.026541699134123683, 0.10749450799069712, 0.10648696371975243, 0.06607455667029914, 0.15313641823651222, 0.0069464874672317605, 0.16485609948747984]

**Best point found**:
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
4096,0,2,0,64,1,7,6,4,16,4194304,-13538


# OLD
# First iteration of paramters, iterations=15
importances: [0.00027195395090342904, 0.20679833603817577, 0.0928234267591486, 0.0, 0.028109540323597172, 0.12197588228681251, 0.021976919936102447, 0.0005799713707593317, 0.004135081340103817, 0.014974478941336161, 0.5083544090530607]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
256,240000,1,1,1,256,7,5,16,4,1073741824,-99430

importances: [0.08060890152776375, 0.0005279025962300257, 0.12601157749412376, 0.07906753438987027, 0.03448487708649841, 0.11450499317925544, 0.005080138146753425, 0.16347769669289983, 0.006673682561023316, 0.0571888615092969, 0.3323738348162849]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
1,240000,2,0,2,128,7,13,2,4,1073741824,-89872

# same as above but increased value choices of write_buffer_size - from skipping powers of 4 to taking every power of 2 in the interval
importances: [0.028081422651937197, 0.00021624914402594046, 0.15998496127389578, 0.0010887195719084012, 0.07824301251477733, 0.003655617334667633, 0.0028401716456740948, 0.06775536964287458, 0.02326016318608497, 0.04923171281919389, 0.5856426002149603]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
512,40000,1,16,512,16,1,5,8,8,536870912,-96509

# above but with readrandomwriterandom and readwrite ratio of 0.5
### Iter=30

importances: [0.030119804474826383, 0.0061254024683540294, 0.2853000654744794, 0.06029117936626131, 0.005726333865639427, 0.009027344257960807, 0.0016283343213978722, 0.021118058467209638, 0.27925120184876123, 0.033917655483681045, 0.26749461997142887]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
256,400000,2,0,8,1,8,9,1,1,536870912,-169423

### Iter=20
importances: [0.06974235367491885, 0.014395343088669658, 0.20735607908053186, 0.03260336928595251, 0.0396108503682212, 0.12608000253372445, 0.0, 0.05372628783316325, 0.039251952734502264, 0.0039332234320908896, 0.41330053796822513]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
1024,40000,4,128,64,256,2,14,16,8,536870912,-170860

importances: [0.1203788248214905, 0.06361469937731319, 0.14361631994396107, 0.019671095229847613, 0.02255541483289674, 0.034493091936110186, 0.04394344611501316, 0.03507666603531896, 0.008217640204652554, 0.005195171326072925, 0.503237630177323]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
1024,0,1,4,128,64,5,0,32,16,536870912,-170536

### Iter=20, but average of 3RUNS and 1M keys instead of 5M
importances: [0.04499982800561807, 0.0021904105687378197, 0.05707468871960688, 0.09848778270350769, 1.4177314947138402e-05, 1.4281759673691843e-05, 0.0011276082973634626, 0.025576423961030475, 0.11624309391508672, 0.006114407591997877, 0.6481572971624301]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
2048,0,1,512,4,128,2,5,2,4,1073741824,-178090

### Iter=28, with threads=32
importances: [0.10795637907328258, 0.06379561620250744, 0.05295660295932644, 0.025401440382893364, 0.02421529070621248, 0.014735352380097549, 0.026522013426623484, 0.04893211654965388, 0.029824601870389458, 0.007360822526870901, 0.5982997639221425]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
2048,400000,1,1024,1024,2,6,10,8,2,67108864,-106245

importances: [0.1119439751349999, 0.008151571469479073, 0.09322092039373825, 0.019688045578462494, 0.03746585707665181, 0.09526071747886242, 0.05975356776463634, 0.04041682370122938, 0.0013221919253613664, 0.0012716022080481253, 0.5315047272685309]
Best point found:
block_size,compaction_readahead_size,level0_file_num_compaction_trigger,level0_slowdown_writes_trigger,level0_stop_writes_trigger,max_background_compactions,max_background_flushes,max_bytes_for_level_multiplier,max_write_buffer_number,min_write_buffer_number_to_merge,write_buffer_size,Throughput
8192,240000,1,1,128,4,1,11,8,2,1073741824,-121661