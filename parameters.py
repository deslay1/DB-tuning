ROCKSDB_PARAMETERS = [
    "block_size",
    "cache_index_and_filter_blocks",
    "compaction_readahead_size",
    "compression_type",
    "level0_file_num_compaction_trigger",
    "level0_slowdown_writes_trigger",
    "level0_stop_writes_trigger",
    "max_background_compactions",
    "max_background_flushes",
    "max_bytes_for_level_multiplier",
    "max_write_buffer_number",
    "min_write_buffer_number_to_merge",
    "write_buffer_size",
]

NEO4J_PARAMETERS = [
    "dbms.memory.heap.max_size",
    "dbms.memory.pagecache.size",
    "dbms.memory.off_heap.max_size",
    "dbms.tx_state.memory_allocation",
    "dbms.memory.pagecache.flush.buffer.enabled",
    "dbms.memory.pagecache.flush.buffer.size_in_pages",
    "dbms.jvm.additional.1",
    "dbms.jvm.additional.2",
    # "dbms.checkpoint.interval.time",
    # "dbms.checkpoint.interval.tx",
]

CASSANDRA_PARAMETERS = [
    # "compaction_method", # causes problems, see output of command `cassandra` after using this
    "compaction_throughput_mb_per_sec",
    "concurrent_compactors",
    "concurrent_reads",
    "concurrent_writes",
    "file_cache_size_in_mb",
    "memtable_heap_space_in_mb",
    "memtable_offheap_space_in_mb",
    "memtable_allocation_type",
    "row_cache_size_in_mb",
    "sstable_preemptive_open_interval_in_mb",
]


def get_parameters(database_type):
    if database_type == "rocksdb":
        return ROCKSDB_PARAMETERS
    elif database_type == "neo4j":
        return NEO4J_PARAMETERS
    elif database_type == "cassandra":
        return CASSANDRA_PARAMETERS
    else:
        return []
