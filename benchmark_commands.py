import os


def run_sequential_random():
    # Creates a db instance in /tmp/... , see terminal output
    os.system('db_bench --benchmarks="fillrandom,readrandom> test.txt"')
