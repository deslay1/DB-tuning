import numpy as np
import os
import project.programs as program
import project.plotters as plot
from dotenv import load_dotenv
from parameters import get_parameters

load_dotenv()


if __name__ == "__main__":

    database_type = os.getenv("DATABASE_TYPE")
    parameters = get_parameters(database_type)

    # Use D + 1 Scheme
    # samples = len(parameters) + 1
    samples = 5 + 1
    # Use 10D scheme
    # optimization_iterations = len(parameters) * 30
    optimization_iterations = 30 * 5

    bench_type = os.getenv("BENCH_TYPE")
    rwpercent = int(os.getenv("READ_WRITE_RATIO_PERCENT", "-1"))

    custom_output_path = os.getenv("CUSTOM_OUTPUT_PATH")
    hm_output_path = os.getenv("HM_OUTPUT_PATH")

    optimizer_options = {
        "db_parameters": parameters,
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
        repetitions=3,
    )

    # program.cassandara_hypermapper(
    #     optimizer_options=optimizer_options,
    #     bench_type="ycsb",
    #     read_write_percent=50,
    #     file_name=hm_output_path,
    #     simple_file_name=custom_output_path,
    #     repetitions=1,
    # )
    # run using sudo ~/anaconda3/envs/tuner/bin/python main.py

    # program.neo4j_default(bench_type=bench_type)
    # program.neo4j_explore(bench_type=bench_type, runs=5)

    # program.neo4j_hypermapper(
    #     optimizer_options=optimizer_options, bench_type=bench_type
    # )
    # run using sudo env "PATH=$PATH" python main.py OR
    # sudo ~/anaconda3/envs/tuner/bin/python main.py
    # sudo ~/anaconda3/envs/lsqb/bin/python main.py

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
