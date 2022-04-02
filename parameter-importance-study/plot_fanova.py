import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import json


HORIZONTAL = False
key = "postgres"
results_file = f"./CAVE/output/{key}/30D_wikipedia.json"
output_format = "eps"
output_image = f"./CAVE/output/{key}/fanova_wikipedia" + f".{output_format}"
ratio = "9:1"
title = f"Read/write ratio {ratio}"

# parameters = [
#     "block_size",
#     "cache_index_and_filter_blocks",
#     "compaction_readahead_size",
#     "compression_type",
#     "level0_file_num_compaction_trigger",
#     "level0_slowdown_writes_trigger",
#     "level0_stop_writes_trigger",
#     "max_background_compactions",
#     "max_background_flushes",
#     "max_bytes_for_level_multiplier",
#     "max_write_buffer_number",
#     "min_write_buffer_number_to_merge",
#     "write_buffer_size",
# ]

parameters = sorted([
        "shared_buffers",
        "work_mem",
        "random_page_cost",
        "effective_io_concurrency",
        "max_wal_size",
        "max_parallel_workers_per_gather",
        "max_parallel_workers",
        "max_worker_processes",
        "checkpoint_timeout",
        "checkpoint_completion_target",
        "effective_cache_size",
        "temp_buffers",
        "wal_buffers",
        "bgwriter_lru_maxpages",
        "bgwriter_delay",
        "default_statistics_target",
        "deadlock_timeout"
    ])


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
ax.barh(
        keys,
        imps,
        label="fANOVA weight",
    )

# Plot threshold
# ax.plot([0., len(parameters)], [threshold, threshold], "k")
# ax.axhline(y=threshold, linewidth=1, color="k", label=f"{threshold*100}%-level")

ax.set_xlabel("Importance weight",fontsize=12)
ax.set_ylabel("Contributing term", fontsize=12)
# ax.set_xticks([t + width for t in range(len(parameters))])
ax.set_yticks(np.arange(len(keys)))
ax.set_yticklabels(keys)
ax.legend()
# plt.tight_layout()
plt.close()
fig.savefig(output_image, bbox_inches="tight", format=output_format)
