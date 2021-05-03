import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import os

import config

plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

normalize = True
output_ops_path = 'optimizer-output/1_throughput_3.png' if not normalize else 'optimizer-output/1_throughput_3_norm.png'
output_importance_path = 'optimizer-output/1_feature_importance_3.png'
files = ['optimizer-output/' + file for file in ['1_mixgraph.csv', '1_mixgraph_2.csv']]

# MANUAL WORK FOR NOW, add the vector from the printed output or log file if that is available.
imps = [
    [0.3407670474741084, 0.01706067975979753, 0.23038264182710874, 0.002729358980699036, 0.09511747315795435, 0.08210144795297077, 0.008928392789567386, 0.016076557274410964, 0.0031041338907908974, 0.0014384009909340766, 0.2022938659016579],
    [0.2231962367872672, 0.0, 0.010535100772364086, 0.13473192973427256, 0.026541699134123683, 0.10749450799069712, 0.10648696371975243, 0.06607455667029914, 0.15313641823651222, 0.0069464874672317605, 0.16485609948747984]
]

# Parse dataframes
dfs = []
for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

#################### 1 - PLOT THROUGHPUTS ####################
x = np.linspace(0, dfs[0].shape[0], num=dfs[0].shape[0])
objectives = []
for df in dfs:
    y = -1*df[config.OPTIMIZATION_OBJECTIVE[0]]
    # 1. We want to see the convergence, so we transform the throughput values to show only BEST SO FAR
    for i in range(1, len(y)):
        if y[i-1] > y[i]:
            y[i] = y[i-1]
    # 2. Normalize values
    if normalize:
        y_min, y_max = min(y), max(y)
        y = [((yi - y_min) / (y_max - y_min) ) for yi in y]
    objectives.append(y)

colors = ['firebrick', 'forestgreen', 'royalblue']
labels = ['1_mixgraph', '1_mixgraph_2']
for i, y in enumerate(objectives):
    plt.plot(x, y, color=colors[i], label=labels[i])
plt.ylabel('Throughput (ops/sec)')
plt.xlabel('Optimizer iteration')
plt.legend()
plt.savefig(output_ops_path, bbox_inches='tight')
plt.close()

plt.cla()

#################### 2 - PLOT FEATURE IMPORTANCES ####################
parameters = config.INPUT_PARAMETERS
fig, ax = plt.subplots()
for i in range(len(objectives)):
    ax.bar(parameters, imps[i], color=colors[i], label=labels[i])
    # bar2 = ax.bar(parameters, importances, color=colors[i], label='')
    # bar3 = ax.bar(parameters, importances, color=colors[i], label='')
ax.set_ylabel('Throughput (ops/sec)')
ax.set_xticks(range(len(parameters)))
ax.set_xticklabels(parameters, rotation=90)
ax.set_title('Convergence rates for different workload benchmarks')
ax.legend()
fig.savefig(output_importance_path, bbox_inches='tight')
plt.close()


# importances = [0.1119439751349999, 0.008151571469479073, 0.09322092039373825, 0.019688045578462494, 0.03746585707665181, 0.09526071747886242, 0.05975356776463634, 0.04041682370122938, 0.0013221919253613664, 0.0012716022080481253, 0.5315047272685309]
# plt.bar(parameters, importances, color='maroon')
# plt.xticks(parameters, rotation=90)
# plt.savefig(f'optimizer-output/{file[:-4]}_params_{img_index}.png', bbox_inches='tight')
# plt.close()