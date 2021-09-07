#!/bin/bash
source $HOME/ubuntu/anaconda3/etc/profile.d/conda.sh
conda activate tuner
python main.py

# Run in background using: nohup ./background.sh > /dev/null 2>&1&