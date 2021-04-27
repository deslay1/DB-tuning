

Best parameters found: **{'block_size': 32768, 'compaction_readahead_size': 120000, 'level0_file_num_compaction_trigger': 32, 'max_background_compactions': 4, 'max_background_flushes': 7, 'write_buffer_size': 536870912}**  
Throughput for above parameters: **({'Throughput': 139375.0}, {'Throughput': {'Throughput': 0.0}})**  

## April 26 results, write buffer size seems most important

{'block_size': 8192, 'compaction_readahead_size': 40000, 'level0_file_num_compaction_trigger': 8, 'max_background_compactions': 1, 'max_background_flushes': 9, 'write_buffer_size': 536870912}
({'Throughput': 151628.0}, {'Throughput': {'Throughput': 0.0}})

{'block_size': 32768, 'compaction_readahead_size': 160000, 'level0_file_num_compaction_trigger': 128, 'max_background_compactions': 256, 'max_background_flushes': 10, 'write_buffer_size': 536870912}
({'Throughput': 151378.0}, {'Throughput': {'Throughput': 0.0}})