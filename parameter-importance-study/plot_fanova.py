import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import json


STACKED = True
HORIZONTAL = False
results_file = "./CAVE/output/30D_rw90.json"
output_image = "./CAVE/output/30D_rw90.eps"
output_image = "fanova.eps"
ratio = "9:1"
title = f"Read/write ratio {ratio}"

parameters = [
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


def format(d):
    new = d.copy()
    for x in d:

        # round numbers to some signifcant figures
        new[x] = round(new[x], 4)

        # if x not in parameters:
        #     del new[x]

    for x in parameters:
        if x not in d:
            new[x] = 0.0

    # weights = np.array(list(dict(sorted(new.items())).values()))
    # weights /= weights.sum() # Normalize
    # return weights.tolist()

    return new


#################### PLOT FEATURE IMPORTANCES ####################
with open(results_file) as f:
    data = json.load(f)
    fANOVA = format(data["fanova"]["imp"])
    imps = list(fANOVA.values())
    keys = list(fANOVA.keys())



threshold = 0.02
colors = ["firebrick", "forestgreen", "royalblue", "purple"]
hatches = ["\\\\", "||", "//", "OO"]
# labels = [f"test - " + str(x) for x in range(1, 4)]


fig, ax = plt.subplots()
width = 0.2
r1 = np.arange(len(imps))
ax.bar(
        keys,
        imps,
        label="fANOVA weight",
    )

# Plot threshold
# ax.plot([0., len(parameters)], [threshold, threshold], "k")
# ax.axhline(y=threshold, linewidth=1, color="k", label=f"{threshold*100}%-level")

ax.set_ylabel("Importance weight")
# ax.set_xticks([t + width for t in range(len(parameters))])
ax.set_xticklabels(parameters, rotation=45)
ax.legend()
plt.tight_layout()
plt.close()
fig.savefig(output_image, bbox_inches="tight", format="eps")
