import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

optimization_cycle = 2
output_ops_path = f'optimizer-output/{optimization_cycle}_throughput'
# output_importance_path = 'optimizer-output/1_feature_importance_3.png'
files = [f'optimizer-output/{optimization_cycle}_' +
         file for file in ['optimizer_10-90.csv', 'optimizer_50-50.csv', 'optimizer_90-10.csv']]

additional = True
additional = {
    2: [f'optimizer-output/{optimization_cycle}_' +
        file for file in ['optimizer_2_10-90.csv', 'optimizer_2_50-50.csv', 'optimizer_2_90-10.csv']],
    3: [f'optimizer-output/{optimization_cycle}_' +
        file for file in ['optimizer_3_10-90.csv', 'optimizer_3_50-50.csv', 'optimizer_3_90-10.csv']]
}

# Parse dataframes
y_store = []
for workload_ind, file in enumerate(files):
    y = []
    df = pd.read_csv(file)
    tps = df.loc[:, 'Throughput']
    y.append(tps.values)
    # additional throughput columns
    if additional:
        for sequence in additional.items():
            add_df = pd.read_csv(sequence[1][workload_ind])
            tps = add_df.loc[:, 'Throughput']
            y.append(tps.values)
            # df = df.join(add_df['Throughput'], how='right',
            #  rsuffix=f'_{sequence[0]}')
    # last throughout column should be the mean
    y.append(np.mean(y, axis=0))
    # store workload throughputs
    y_store.append(y)

# print(y_store[2][0][-10:])
# print(y_store[2][1][-10:])
# print(y_store[2][2][-10:])
# print(len(y_store))
# print(len(y_store[0][0]))

#################### PLOT THROUGHPUTS ####################
iterations = len(y_store[0][0])
x = np.linspace(0, iterations, num=iterations)
colors = ['firebrick', 'forestgreen', 'royalblue', 'lightgray']
labels = ['10/90', '50/50', '90/10']
for workload_ind, workload_y in enumerate(y_store):
    workload_y = [-1*y_i for y_i in workload_y]

    # We want to see the convergence, so we transform the throughput values to show only BEST SO FAR
    for y_i in workload_y:
        for i in range(1, len(y_i)):
            if y_i[i-1] > y_i[i]:
                y_i[i] = y_i[i-1]

    # plot additional as gray lines, and contrast the mean line with a strong color
    for i in range(len(workload_y)-1):
        plt.plot(x, workload_y[i], color=colors[-1])
    plt.plot(x, workload_y[-1], color=colors[0], label='HyperMapper')
    plt.axhline(y=workload_y[-1][0], linewidth=3, color='k',
                label='Default')
    # increase = int(((y.iloc[-1] - y[0]) / y[0]) * 100)
    # plt.axhline(y=y.iloc[-1], linewidth=3, color=colors[1],
    #             label=f'Max: {y.iloc[-1]} ≈ {increase}%-increase')
    plt.ylabel('Throughput (ops/sec)')
    plt.xlabel('Optimizer iteration')
    plt.title(f'RRWR - {labels[workload_ind]}')
    plt.legend()
    plt.savefig(f'{output_ops_path}_{workload_ind+1}.png', bbox_inches='tight')
    plt.close()
    plt.cla()
