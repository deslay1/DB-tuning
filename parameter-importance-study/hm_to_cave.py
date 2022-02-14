"""
Script that formats the results and scenario of a HyperMapper optimization sequence to files supported by CAVE.
"""
# 1
# CAVE keyword : (->) HM keyword
# cost : [objective name]
# time : runtime to evaluate a configuration - in our case not really applicable so use a constant
# param1: param1...

import os
import pandas as pd
import json
import pathlib
from shutil import copyfile

key = "postgres"
results_dir = f"CAVE/{key}/results/"
cave_dir = f"CAVE/{key}/"
search_space_file = f"CAVE/{key}/search_space_{key}.json"

for _, file in enumerate([x for x in os.listdir(results_dir) if x.endswith(".csv")]):
    hm_df = pd.read_csv(results_dir + file)
    hm_df = hm_df.drop(columns=["Timestamp"])
    hm_df = hm_df.rename(columns={"Throughput": "cost"})
    cave_df = pd.DataFrame(data=hm_df)
    trajectory_df = cave_df.copy()
    cave_df["time"] = [0.1] * len(hm_df)
    cave_df["status"] = ["SUCCESS"] * len(hm_df)
    cave_df["seed"] = [1] * len(hm_df)
    # cave_df = cave_df.reset_index()

    # Create trajectory file
    trajectory_df["cpu_time"] = [0.1] * len(hm_df)
    trajectory_df["wallclock_time"] = [0.1] * len(hm_df)
    trajectory_df["evaluations"] = [0] * len(hm_df)
    cost_array = trajectory_df["cost"].tolist()
    prev_best = cost_array[0]
    prev_best_index = 0
    drop_indices = []
    for ind, cost in enumerate(cost_array):
        if cost < prev_best:
            # update trajectory row
            trajectory_df.iloc[ind]["evaluations"] = ind
            prev_best = cost
            prev_best_index = ind
        else:
            if ind > 0:
                drop_indices.append(ind)
    trajectory_df = trajectory_df.drop(drop_indices)

    instance_path = cave_dir + file[:-4] + "/"
    pathlib.Path(instance_path).mkdir(parents=True, exist_ok=True)
    cave_df.to_csv(instance_path + "runhistory.csv", index=False)
    trajectory_df.to_csv(instance_path + "trajectory.csv", index=False)

    # copy over scneario file
    copyfile(cave_dir + "scenario.txt", instance_path + "scenario.txt")


# 2. Format configuration space
# {hyperparameters: [ {param1}, {param2} ]}

configspace = {"hyperparameters": []}
with open(search_space_file) as f:
    data = json.load(f)  #  dict
    for param in data.items():
        entry = {}
        entry["name"] = param[0]
        print(param)
        if param[1]["parameter_type"] in ("integer", "real"):
            if param[1]["parameter_type"] == "integer":
                entry["type"] = "uniform_int"
            else:
                entry["type"] = "uniform_float"
            entry["log"] = False
            values = param[1]["values"]
            entry["lower"] = values[0]
            entry["upper"] = values[1]
            entry["default"] = param[1]["parameter_default"]
        else:  # categorical or ordinal -> categorical in CAVE
            entry["type"] = "categorical"

            if param[1]["parameter_default"] in ("false", "true"):
                entry["choices"] = ["False", "True"]
                entry["default"] = (
                    "False" if param[1]["parameter_default"] == "false" else "True"
                )
            else:
                entry["choices"] = [str(x) for x in param[1]["values"]]
                entry["default"] = str(param[1]["parameter_default"])
            entry["probabilities"] = None

        configspace["hyperparameters"].append(entry)

configspace["conditions"] = []
configspace["forbiddens"] = []

with open(cave_dir + "configspace.json", "w") as f:
    json.dump(configspace, f, indent=2, ensure_ascii=False)
