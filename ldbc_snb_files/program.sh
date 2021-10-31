#!/bin/bash
cd "$(dirname "$0")"
for i in {1..5}
do
   . scripts/environment-variables-default.sh;
   scripts/snapshot-load.sh;
   driver/benchmark.sh;
   python3 parse.py;
done