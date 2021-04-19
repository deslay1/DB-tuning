#!/bin/bash
source /home/osama.eldawebi/anaconda3/etc/profile.d/conda.sh
conda activate tuner
rm -r /tmp/rocksdb-bench/
python run_optimizer.py