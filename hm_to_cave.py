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

results_dir = "output/feature_importance/"
cave_dir = "output/feature_importance/CAVE/"

# Convert all first-run files that end in 1.csv
for file in [x for x in os.listdir(results_dir) if x.endswith("1.csv")]:
    hm_df = pd.read_csv(results_dir + file)
    cave_df = pd.DataFrame(data=hm_df)
    cave_df = cave_df.rename(columns={"Throughput": "cost"})
    cave_df["time"] = [0.1] * len(hm_df)
    cave_df["status"] = ["SUCCESS"] * len(hm_df)
    cave_df["seed"] = [1] * len(hm_df)
    cave_df = cave_df.drop(columns=["Timestamp"])
    # cave_df = cave_df.reset_index()

    cave_df.to_csv(cave_dir + file, index=False)


# 2. Format configuration space
# {hyperparameters: [ {param1}, {param2} ]}

import json

configspace = {"hyperparameters": []}
with open("util/search_space.json") as f:
    data = json.load(f)  #  dict
    for param in data.items():
        entry = {}
        entry["name"] = param[0]
        if param[1]["parameter_type"] == "integer":
            entry["type"] = "uniform_int"
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
