import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

optimization_cycle = 2
output_ops_path = f'optimizer-output/{optimization_cycle}_throughput_ver2'
# output_importance_path = 'optimizer-output/1_feature_importance_3.png'
files = [f'optimizer-output/{optimization_cycle}_' +
         file for file in ['optimizer_3_10-90.csv', 'optimizer_3_50-50.csv', 'optimizer_3_90-10.csv']]

latency_cycle = 1
latency_files = [f'optimizer-output/latencies_pruned_{latency_cycle}_' + file for file in [
    '10-90.md', '50-50.md', '90-10.md']]

additional = True
additional = {
    # 2: [f'optimizer-output/{optimization_cycle}_' +
    #     file for file in ['optimizer_2_10-90.csv', 'optimizer_2_50-50.csv', 'optimizer_2_90-10.csv']],
    # 3: [f'optimizer-output/{optimization_cycle}_' +
    #     file for file in ['optimizer_3_10-90.csv', 'optimizer_3_50-50.csv', 'optimizer_3_90-10.csv']],
    4: [f'optimizer-output/{optimization_cycle}_' +
        file for file in ['optimizer_4_10-90.csv', 'optimizer_4_50-50.csv', 'optimizer_4_90-10.csv']],
    5: [f'optimizer-output/{optimization_cycle}_' +
        file for file in ['optimizer_5_10-90.csv', 'optimizer_5_50-50.csv', 'optimizer_5_90-10.csv']],
}

# Parse TPS from csv files
y_store = []
means_with_errors = []
best_workload_indices = [[0], [0], [0]]
for workload_ind, file in enumerate(files):
    y = []
    df = pd.read_csv(file)
    tps = -1 * df.loc[:, 'Throughput']
    y.append(tps.values)

    # additional throughput columns
    if additional:
        for sequence in additional.items():
            add_df = pd.read_csv(sequence[1][workload_ind])
            tps = -1 * add_df.loc[:, 'Throughput']
            y.append(tps.values)
            # df = df.join(add_df['Throughput'], how='right',
            #  rsuffix=f'_{sequence[0]}')

    # We want to see the convergence, so we transform the throughput values to show only BEST SO FAR
    for iter_1, y_i in enumerate(y):
        for i in range(1, len(y_i)):
            if y_i[i-1] > y_i[i]:
                if iter_1 == 2:
                    best_workload_indices[workload_ind].append(
                        best_workload_indices[workload_ind][-1])
                y_i[i] = y_i[i-1]
            else:
                if iter_1 == 2:
                    best_workload_indices[workload_ind].append(i)

    # add mean with error bars
    res = []
    means = np.mean(y, axis=0)
    maxs = np.max(y, axis=0)
    mins = np.min(y, axis=0)
    res.append(means)
    res.append(maxs)
    res.append(mins)
    # 95% confidence interval
    # error = 1.96 * np.std(means) / np.mean(means)
    # res.append(error)
    # print(res)
    means_with_errors.append(res)

    # store workload throughputs
    y_store.append(y)


# Parse Latency values from MD files
l_workloads = []
for w_ind, file in enumerate(latency_files):
    l = []
    with open(file) as f:
        for line_ind, line in enumerate(f.readlines()):
            values = line.split(',')
            if len(values) > 1:
                read_latency = float(np.round(float(values[1]), 2))
                l.append(read_latency)

    # save latencies correponding to best TPS so far
    for i in range(1, len(l)):
        l[i] = l[best_workload_indices[w_ind][i]]

    # Add latencies for plotting
    l_workloads.append(l)


#################### PLOT THROUGHPUTS ####################
iterations = len(y_store[0][0])
x = np.linspace(0, iterations, num=iterations)
colors = ['firebrick', 'forestgreen', 'royalblue', 'lightgray']
labels = ['10/90', '50/50', '90/10']
legend_locs = [7, 1, 7]
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

for workload_ind, workload_y in enumerate(y_store):
    workload_y = [y_i for y_i in workload_y]

    # plot additional as gray lines, and contrast the mean line with a strong color
    # for i in range(len(workload_y)-1):
    #     plt.plot(x, workload_y[i], color=colors[-1])

    upper_bound = means_with_errors[workload_ind][1]
    upper_error = np.abs(means_with_errors[workload_ind][1] -
                         means_with_errors[workload_ind][0])
    lower_bound = means_with_errors[workload_ind][2]
    lower_error = np.abs(means_with_errors[workload_ind][0] -
                         means_with_errors[workload_ind][2])
    # plt.errorbar(x, means_with_errors[workload_ind]
    #              [0], yerr=[lower_error, upper_error], color=colors[0], label='HyperMapper', ecolor='lightsteelblue')
    ax1.plot(x, means_with_errors[workload_ind]
             [0], color=colors[0], label='HyperMapper')
    ax1.fill_between(x, lower_bound, upper_bound, color='b', alpha=.1)
    ax1.axhline(y=means_with_errors[workload_ind][0][0], linewidth=1, color='k',
                label='Default')
    ax1.set_ylabel('Throughput (ops/s)')
    ax1.set_xlabel('Optimizer iteration')
    ax1.set_title(f'RRWR - {labels[workload_ind]}')
    # Legend for hidden plot for latency so we get one legend
    ax1.plot(np.nan, '-r', color=colors[2], label='Read latency')
    ax1.legend(loc=legend_locs[workload_ind])

    ax2.plot(x, l_workloads[workload_ind],
             color=colors[2], label='Read latency')
    ax2.set_ylabel(r'Read latency ($\mu$s)')
    # ax2.legend()
    fig.savefig(f'{output_ops_path}_{workload_ind+1}_test.png',
                bbox_inches='tight')
    # ax1.close()
    ax1.cla()
    ax2.cla()
