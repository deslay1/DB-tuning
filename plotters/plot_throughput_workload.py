import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import pdb

# plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

optimization_cycle = 2
output_ops_path = 'snic-test/test_50_50.png'

workload_files = [f'snic-test/RUN_1_{i}.csv' for i in range(1,11)]

# Parse TPS from csv files
y = []
means_with_errors = []
for file in workload_files:
    df = pd.read_csv(file, header=None, names=['Throughput', 'Latency'])
    tps = df.iloc[:, 0].values
    # Update with only best so far
    prev = tps[0]
    for i in range(1, len(tps)):
        if tps[i] < prev:
            tps[i] = prev
        prev = tps[i]
    
    y.append(tps)

# add mean with error bars
res = []
means = np.mean(y, axis=0)
maxs = np.max(y, axis=0)
mins = np.min(y, axis=0)
res.append(means)
res.append(maxs)
res.append(mins)
pdb.set_trace()


#################### PLOT THROUGHPUTS ####################
iterations = len(y[0])
x = np.linspace(0, iterations, num=iterations)
colors = ['firebrick', 'forestgreen', 'royalblue', 'lightgray']
labels = ['10/90', '50/50', '90/10']
# legend_locs = [7, 1, 7]
fig, ax1 = plt.subplots()

# plot additional as gray lines, and contrast the mean line with a strong color
# for i in range(len(workload_y)-1):
#     plt.plot(x, workload_y[i], color=colors[-1])

upper_bound = res[1]
upper_error = np.abs(res[1] - res[0])
lower_bound = res[2]
lower_error = np.abs(res[0] - res[2])
# plt.errorbar(x, means_with_errors[workload_ind]
#              [0], yerr=[lower_error, upper_error], color=colors[0], label='HyperMapper', ecolor='lightsteelblue')
ax1.plot(x, res[0], color=colors[0], label='DBtune')
ax1.fill_between(x, lower_bound, upper_bound, color='b', alpha=.1)
ax1.axhline(y=res[0][0], linewidth=1, color='k',
            label='Default')
ax1.set_ylabel('Throughput (ops/s)')
ax1.set_xlabel('Optimizer iteration')
ax1.set_title('SNIC test with RRWR - 50/50')
# Legend for hidden plot for latency so we get one legend
# ax1.plot(np.nan, '-r', color=colors[2], label='Read latency')
fig.savefig(f'{output_ops_path}', bbox_inches='tight')
# ax1.close()
ax1.cla()
