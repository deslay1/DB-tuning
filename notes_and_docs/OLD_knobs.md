## Categorical variables might be interesting  - 26/4/2021
- For example those associated with bloom filters
- They integrate well with HyperMapper
- Look into cache_index_and_filter_block: true or false

Possibly good parameters:
- cache_index (bloom filters): https://github.com/facebook/rocksdb/wiki/RocksDB-Tuning-Guide#bloom-filters
- number of open files for bloom filters controlled by max_open_files, which is set to -1 by default (all files open in memory).
- filter policy : first in https://github.com/facebook/rocksdb/wiki/RocksDB-Tuning-Guide#general-options
Sets bloom filters on, default is null(?). value is number of bits per key, the higher the less false positive rate but more memory usage and space amplification.


# Tunings knobs that could be important - pre-26/4/2021
## RocksDB
### Most relevant: paper by Sami Alabed: https://arxiv.org/pdf/2103.16267.pdf 
Includes 10 parameters, some of which are included in the paper below. This project will use all 10 from this paper.

### The paper *Optimization of RocksDB for Redis on Flash* by Ouaknine et al. (2017) determines the following knobs as important (excluding any Redis knobs):

*Name-default value-value used-performance impact*
- compaction_readahead_size-0-2MB-300%
- block_size-4k-16k-60%
- max_background_compactions-8-64-24%
- level0_slowdown_writes_trigger-12-24-10%
- level0_stop_writes_trigger-20-40-10%
- optimize_filters_for_hits-false-true-7%

The default values have most likely changed since the paper was published 4 year ago.

## Cassandra & PostgreSQL
5 Knobs (for each test) identified in *Too Many Knobs to Tune* by Kanellis et al. (2020) for the Cassandra and Postgres with YCSB-A and YCSB-B (though impact of each knob varies for different workloads):

Cassandra, in order of importance:
- concurrent_reads
- native_transport_max_threads
- memtable_heap_space_in_mb
- memtable_cleanup_threshold
- compaction_throughput_mb_per_sec

Postgres (excluding statistics) for YCSB-A:
- fsync
- shared_buffers
- wal_sync_method
- commit_delay
- work_mem


Postgres (excluding statistics) for YCSB-B:
- fsync
- wal_sync_method
- shared_buffers
- backend_flush_after
- commit_delay