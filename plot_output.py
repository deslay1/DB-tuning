import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import os

import config

plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

normalize = False
output_ops_path = 'optimizer-output/1_throughput_2.png' if not normalize else 'optimizer-output/1_throughput_2_norm.png'
output_importance_path = 'optimizer-output/1_feature_importance_2.png'
files = ['optimizer-output/' + file for file in ['readrandomwriterandom50_2.csv', 'updaterandom50.csv', 'readrandom50.csv']]

# MANUAL WORK FOR NOW, add the vector from the printed output or log file if that is available.
imps = [
    [0.055445107303136155, 0.048877700628293136, 0.01929532842262805, 0.13084902528584758, 0.023027046103120306, 0.02813681783435002, 0.021166692624159107, 0.009288342610501783, 0.00403001343594297, 0.00670673010188481, 0.6531771956501362],
    [0.15385905108085335, 0.008006894642432242, 0.00540808190366646, 0.000516770446485539, 0.0798487068106021, 0.03331838540360432, 0.003290172332434804, 0.03354940429782523, 0.03600661420363871, 0.008655696717949395, 0.6375402221605079],
    [0.3812921587681154, 0.024027374605416867, 0.11893936120198154, 0.0009652864466218999, 0.027704099012557624, 0.007727132095317659, 0.006051348600476096, 0.003353719444603654, 0.007245856209043429, 0.008801271384755359, 0.4138923922311105]

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
labels = ['readrandomwriterandom', 'updaterandom', 'readrandom']
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