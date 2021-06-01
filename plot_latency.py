import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


default_rl = []
default_wl = [701.03, 704.09, 707.44]

best_rl = []
best_wl = [676.05, 719.70, 662.95]

std = [np.std(default_wl), np.std(best_wl)]
values = [np.mean(default_wl), np.mean(best_wl)]

error = np.int0([std[0], std[1]])
plt.figure(figsize=(10, 6))
# plt.suptitle('RocksDB', size=20)
plt.title('RRWR (r/w - 50/50)', size=17)
# plt.grid(axis='y',zorder=0)
plt.ylim((0, 800))
plt.ylabel('Write latency' + r'($\mu$s)', size=15)
plt.bar(np.arange(2), height=values, color=[
        'grey', 'firebrick'], yerr=error, capsize=7, zorder=3, width=0.6)
plt.xticks(np.arange(2), ['Default', 'DBtune'], size=15)

for index, value in enumerate(values):
    plt.text(index-0.065, value+1000, str(value), size=15)

plt.show()
