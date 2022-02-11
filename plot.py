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

    results = [f"output/final/feat_imp/reduced_fixed_rw50_{x}.csv" for x in range(1, 4)]

    # plot.throughput_from_custom(input_files=results)
    plot.throughput_multiple(format="png")

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
