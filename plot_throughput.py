import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import config

plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

optimization_cycle = 2
normalize = False
output_ops_path = f'optimizer-output/{optimization_cycle}_throughput' if not normalize else f'optimizer-output/{optimization_cycle}_throughput_norm'
# output_importance_path = 'optimizer-output/1_feature_importance_3.png'
files = [f'optimizer-output/{optimization_cycle}_' +
         file for file in ['optimizer_10-90.csv', 'optimizer_50-50.csv', 'optimizer_90-10.csv']]

# MANUAL WORK FOR NOW, add the vector from the printed output or log file if that is available.
# instance 1, instance 2, instance 3 - readwrite-ratio: 50/50, 10/90, 90/10
# imps = [
#     [0.0834566154693668, 0.07086988807162646, 0.03723598751758941, 0.05016996005946036, 0.013130122470113265, 0.02225278424022249, 0.011933185602351295,
#         0.34295533143658197, 0.16889271965639352, 0.1825389287044095, 0.014976061812265833, 0.0012939531666693322, 0.00029446179294972995],
#     [0.12029732118097443, 0.04668639161903948, 0.026640798448042978, 0.07261161123727286, 0.015070488156516302, 0.01756198756993836, 0.00864525450699469,
#         0.4489157809663446, 0.1388029367370333, 0.07107049232606212, 0.0031564098926242313, 0.013401878970432457, 0.017138648388724257],
# ]

# Parse dataframes
dfs = []
for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

#################### PLOT THROUGHPUTS ####################
x = np.linspace(0, dfs[0].shape[0], num=dfs[0].shape[0])
colors = ['firebrick', 'forestgreen', 'royalblue']
labels = ['r/w - 10/90', 'r/w - 50/50', 'r/w - 90/10']
for df_ind, df in enumerate(dfs):
    y = -1*df[config.OPTIMIZATION_OBJECTIVE[0]]
    # 1. We want to see the convergence, so we transform the throughput values to show only BEST SO FAR
    for i in range(1, len(y)):
        if y[i-1] > y[i]:
            y[i] = y[i-1]
    # 2. Normalize values
    if normalize:
        y_min, y_max = min(y), max(y)
        y = [((yi - y_min) / (y_max - y_min)) for yi in y]

    # plt.plot(x, obj, color=colors[i], label=labels[i])
    plt.plot(x, y, color=colors[0], label=labels[df_ind])
    # plt.hlines(y=y[0], lw=2, label='Baseline')
    plt.axhline(y=y[0], linewidth=3, color='k',
                label=f'Baseline: {y[0]}')
    increase = int(((y.iloc[-1] - y[0]) / y[0]) * 100)
    plt.axhline(y=y.iloc[-1], linewidth=3, color=colors[1],
                label=f'Max: {y.iloc[-1]} ≈ {increase}%-increase')
    plt.ylabel('Throughput (ops/sec)')
    plt.xlabel('Optimizer iteration')
    plt.title('Convergence rates')
    plt.legend()
    plt.savefig(f'{output_ops_path}_{df_ind+1}.png', bbox_inches='tight')
    plt.close()
    plt.cla()
