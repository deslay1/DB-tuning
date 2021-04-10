Nothing:
Throughput (ops/sec): 83974

Two knobs - compaction_readahead_size and max_background_compactions (values 8 and 0 in order):
Throughput (ops/sec): 85930
Throughput (ops/sec): 85745
Throughput (ops/sec): 84819
Manually calculated average: 85498

Two knobs - compaction_readahead_size and max_background_compactions (values 32 and 1024 in order):
Throughput (ops/sec): 85320
Throughput (ops/sec): 85451
Throughput (ops/sec): 85110
Manually calculated average: 85294

Two knobs - compaction_readahead_size and max_background_compactions (values 64 and 2048 in order):
Throughput (ops/sec): 85893
Throughput (ops/sec): 84935
Throughput (ops/sec): 85919
Manually calculated average: 85582

Two knobs - compaction_readahead_size and max_background_compactions (values 64 and 2000000 in order):
Throughput (ops/sec): 83929
Throughput (ops/sec): 85751
Throughput (ops/sec): 86808
Manually calculated average: 85496