#!/bin/bash
source /home/osama.eldawebi/anaconda3/etc/profile.d/conda.sh
conda activate tuner
python run_tests.py
# python run_optimizer.py
git add -A
git commit -m "performed threading tests"
git push