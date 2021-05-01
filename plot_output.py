import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import sys
import os

import config

plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')

try:
    file = sys.argv[1]
    df = pd.read_csv(file)
except:
    print('An error has occurred, either no file has been passed as an argument or the file does not exist.')
    sys.exit(0)

x = np.linspace(0, df.shape[0], num=df.shape[0])
y = -1*df[config.OPTIMIZATION_OBJECTIVE[0]]
# We want to see the convergence, so we transform the throughput values to show only BEST SO FAR
for i in range(1, len(y)):
    if y[i-1] > y[i]:
        y[i] = y[i-1]

plt.plot(x, y, color='navy')
plt.ylabel('Throughput (ops/sec)')
plt.xlabel('Optimizer iteration')
# plt.show()
img_index = 1
while os.path.exists(f'{file[:-4]}_{img_index}.png'):
    img_index += 1

plt.savefig(f'optimizer-output/{file[:-4]}_{img_index}.png', bbox_inches='tight')
plt.close()

# MANUAL WORK FOR NOW, so uncomment when you want the feature importance graph and 
# add the vector from the log file or printed output if that is available.

plt.cla()

parameters = config.INPUT_PARAMETERS
importances = [0.1119439751349999, 0.008151571469479073, 0.09322092039373825, 0.019688045578462494, 0.03746585707665181, 0.09526071747886242, 0.05975356776463634, 0.04041682370122938, 0.0013221919253613664, 0.0012716022080481253, 0.5315047272685309]
y_pos = range(len(parameters))
plt.bar(parameters, importances, color='maroon')
plt.xticks(parameters, rotation=90)
plt.savefig(f'optimizer-output/{file[:-4]}_params_{img_index}.png', bbox_inches='tight')
plt.close()