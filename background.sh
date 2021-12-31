#!/bin/bash
# source $HOME/anaconda3/etc/profile.d/conda.sh
source /home/ubuntu/anaconda3/bin/activate tuner
python main.py

# Run in background using: sudo nohup ./background.sh > /dev/null 2>&1&