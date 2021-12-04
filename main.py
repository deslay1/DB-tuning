import project.programs as program
import project.plotters as plot
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

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

# INPUT_PARAMETERS = [
#     "dbms.memory.heap.max_size",
#     "dbms.memory.pagecache.size",
#     "dbms.memory.off_heap.max_size",
#     "dbms.tx_state.memory_allocation",
#     "dbms.memory.pagecache.flush.buffer.enabled",
#     "dbms.memory.pagecache.flush.buffer.size_in_pages",
#     "dbms.jvm.additional.1",
#     "dbms.jvm.additional.2",
#     # "dbms.checkpoint.interval.time",
#     # "dbms.checkpoint.interval.tx",
# ]


if __name__ == "__main__":
    # Use D + 1 Scheme
    samples = len(INPUT_PARAMETERS) + 1
    # Use 10D scheme
    optimization_iterations = len(INPUT_PARAMETERS) * 30

    bench_type = os.getenv("BENCH_TYPE")
    rwpercent = int(os.getenv("READ_WRITE_RATIO_PERCENT", "-1"))

    custom_output_path = os.getenv("CUSTOM_OUTPUT_PATH")
    hm_output_path = os.getenv("HM_OUTPUT_PATH")

    optimizer_options = {
        "db_parameters": INPUT_PARAMETERS,
        "num_samples": samples,
        "optimization_iterations": optimization_iterations,
        "doe_type": "random sampling",
        "resume": False,
    }
    program.rocksdb_hypermapper(
        optimizer_options=optimizer_options,
        bench_type=bench_type,
        read_write_percent=rwpercent,
        simple_file_name=custom_output_path,
        file_name=hm_output_path,
        repetitions=1,
    )

    # program.neo4j_default(bench_type=bench_type)
    # program.neo4j_explore(bench_type=bench_type, runs=5)

    # program.neo4j_hypermapper(
    #     optimizer_options=optimizer_options, bench_type=bench_type
    # )
    # run using sudo env "PATH=$PATH" python main.py OR
    # sudo ~/anaconda3/envs/tuner/bin/python main.py

    # program.rocksdb_default(
    #     bench_type=bench_type,
    #     read_write_percent=rwpercent,
    #     simple_file_name=f"output/custom/test_rw{rwpercent}",
    #     file_name=f"test_rw{rwpercent}",
    #     runs=1,
    # )

    ######################## PLOT FEATURE_IMPORTANCE ########################

    # selected_parameters = INPUT_PARAMETERS
    # results_type = "mixgraph"
    # results_folder = "output/feature_importance/custom/"

    # imps = []
    # for name in os.listdir(results_folder):
    #     if results_type in name:
    #         with open(results_folder + name, "r") as f:
    #             lines = f.read().splitlines()
    #             weights = lines[-1][1:-1]  # ignore the brackets
    #             weights = weights.split(",")
    #             weights = [
    #                 float(x) for x in [weights[ind] for ind in range(len(weights))]
    #             ]  # change strings to integers
    #             imps.append(weights)

    # # Calculate the mean of the feature importance experiment results
    # imps = [np.mean(imps, axis=0)]

    # plot.feature_importance(
    #     imps,
    #     selected_parameters,
    #     "output/feature_importance/plots/feature_imps_mixgraph.png",
    #     base_label="mixgraph",
    # )
