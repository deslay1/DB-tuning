from project.config import NUMBER_OF_SAMPLES
import project.programs as pp

INPUT_PARAMETERS = [
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


if __name__ == "__main__":
    # Use 10D scheme
    samples = len(INPUT_PARAMETERS) * 10
    bench_type = "readrandomwriterandom"
    rwpercent = 10

    optimizer_options = {
        "db_parameters": INPUT_PARAMETERS,
        "num_samples": samples,
        "optimization_iterations": 1,
    }
    pp.run_hypermapper(
        optimizer_options=optimizer_options,
        bench_type=bench_type,
        read_write_percent=rwpercent,
        simple_file_name=f"output/custom/full_space_rw{rwpercent}",
        file_name=f"full_space_rw{rwpercent}",
        repetitions=3,
    )

    # pp.run_default(
    #     bench_type=bench_type,
    #     read_write_percent=rwpercent,
    #     simple_file_name=f"output/custom/test_rw{rwpercent}",
    #     file_name=f"test_rw{rwpercent}",
    #     runs=1,
    # )
