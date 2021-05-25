import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


default_rl = []
default_wl = []

best_rl = []
best_wl = []

std = [np.min(best_rl), np.max(best_rl)]
std = [np.min(best_wl), np.max(best_wl)]
error = np.int0([std[0], std[1]])
plt.figure(figsize=(10, 6))
# plt.suptitle('RocksDB', size=20)
plt.title('RRWR (' + r'$\approx$' + '90% Write 10% Read)', size=17)
# plt.grid(axis='y',zorder=0)
plt.ylim((0, 120000))
plt.ylabel('Throughput (ops/s)', size=15)
plt.bar(np.arange(2), height=value, color=[
        'grey', 'firebrick'], yerr=error, capsize=7, zorder=3, width=0.6)
plt.xticks(np.arange(2), ['Default', 'DBTune'], size=15)
for index, value in enumerate(value):
    plt.text(index-0.065, value+1000, str(value), size=15)
