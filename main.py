from project.config import NUMBER_OF_SAMPLES
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


if __name__ == "__main__":
    # Use 10D scheme
    samples = len(INPUT_PARAMETERS) * 10
    # samples = len(INPUT_PARAMETERS) + 1
    optimization_iterations = 1
    # optimization_iterations = 100
    bench_type = os.getenv("BENCH_TYPE")
    rwpercent = int(os.getenv("READ_WRITE_RATIO_PERCENT", "-1"))

    custom_output_path = os.getenv("CUSTOM_OUTPUT_PATH")
    hm_output_path = os.getenv("HM_OUTPUT_PATH")

    print(custom_output_path)
    print(hm_output_path)

    optimizer_options = {
        "db_parameters": INPUT_PARAMETERS,
        "num_samples": samples,
        "optimization_iterations": optimization_iterations,
        "doe_type": "random sampling",
    }

    # program.run_hypermapper(
    #     optimizer_options=optimizer_options,
    #     bench_type=bench_type,
    #     read_write_percent=rwpercent,
    #     simple_file_name=custom_output_path,
    #     file_name=hm_output_path,
    #     repetitions=1,
    # )

    # program.run_default(
    #     bench_type=bench_type,
    #     read_write_percent=rwpercent,
    #     simple_file_name=f"output/custom/test_rw{rwpercent}",
    #     file_name=f"test_rw{rwpercent}",
    #     runs=1,
    # )

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
