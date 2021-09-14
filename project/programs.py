from project.plotters import throughput
from hypermapper import optimizer
from project.benchmark import RocksdbBenchmark
from datetime import datetime
import project.config as config
import subprocess
import pandas as pd
import pdb
import sys
import os
import json

ROOT = os.getcwd()


def setup_optimizer(
    db_parameters, num_samples, optimization_iterations, doe_type, file_name
):
    """
    Creates a json file for the optimizer to use.
    """
    # Update search space file
    with open(f"{ROOT}/util/search_space.json", "w") as file:
        json.dump(config.Knobs, file, indent=4)

    scenario_file = f"{ROOT}/util/optimizer_scenario.json"
    scenario = {}
    scenario["application_name"] = config.APPLICATION_NAME
    scenario["optimization_objectives"] = config.OPTIMIZATION_OBJECTIVE
    scenario["optimization_iterations"] = optimization_iterations
    scenario["models"] = {}
    scenario["models"]["model"] = config.MODEL
    scenario["design_of_experiment"] = {}
    scenario["design_of_experiment"]["doe_type"] = doe_type
    scenario["design_of_experiment"]["number_of_samples"] = num_samples
    scenario["input_parameters"] = {}
    scenario["print_parameter_importance"] = True
    scenario["output_data_file"] = f"{ROOT}/{file_name}.csv"
    scenario["output_image"] = {
        "output_image_pdf_file": config.OUTPUT_IMAGE_FILE,
        "optimization_objectives_labels_image_pdf": ["Throughput (ops/sec)"],
        # 'image_xlog': False,
        # 'image_ylog': True,
    }

    # Load knobs into scenario file
    with open(f"{ROOT}/util/search_space.json", "r") as fobj:
        knobs = json.load(fobj)
        parameter_options = ["parameter_default", "parameter_type", "values"]
        for para in db_parameters:
            scenario["input_parameters"][para] = dict(
                zip(parameter_options, [knobs[para][k] for k in parameter_options])
            )

    with open(scenario_file, "w") as sf:
        json.dump(scenario, sf, indent=4)


def run_benchmark(bench_type, knobs, options, runs=3, database="rocksdb"):
    """
    Calls the appropriate benchmark class and runs the benchmark.
    """
    if database == "rocksdb":
        bench = RocksdbBenchmark(bench_type=bench_type, options=options)
    else:
        bench = RocksdbBenchmark(bench_type=bench_type, options=options)

    # Load if we have specific configurations - otherwise default will be used.
    if knobs:
        knobs = dict((k, str(v)) for k, v in knobs.items())
        bench.load_knob_configurations(knobs)

    if database == "rocksdb":
        throughput, latency = bench.run_benchmark(
            runs=runs,
            num_million=5,
            fill=True,
            options_file=False,
            use_existing=True,
            max_seconds=300,
            calc_latency=True,
        )
    else:
        throughput = 0

    return throughput


def rocksdb_default(
    bench_type="readrandomwriterandom",
    read_write_percent=50,
    simple_file_name="simple_test",
    file_name="test",
    runs=3,
):
    options = {
        "output_file": f"{simple_file_name}.csv",
        "readwritepercent": read_write_percent,
        "threads": 32,
    }
    for _ in range(1):
        tps = run_benchmark(bench_type, {}, options, runs=runs)
        print(tps)


def rocksdb_hypermapper(
    bench_type="readrandomwriterandom",
    read_write_percent=50,
    simple_file_name="simple_test",
    file_name="test",
    repetitions=1,
    optimizer_options={},
):
    run_ind = 0

    def objective_function(knobs):
        options = {
            "output_file": f"{simple_file_name}_{run_ind}.csv",
            "readwritepercent": read_write_percent,
            "threads": 32,
        }
        throughput = run_benchmark(bench_type, knobs, options)
        return -int(throughput)

    for _ in range(repetitions):
        run_ind += 1
        if optimizer_options:
            setup_optimizer(
                optimizer_options["db_parameters"],
                optimizer_options["num_samples"],
                optimizer_options["optimization_iterations"],
                optimizer_options["doe_type"],
                f"{file_name}_{run_ind}",
            )
        optimizer.optimize("util/optimizer_scenario.json", objective_function)
        # Get feat importance
        symbol = "feature importances: "
        with open(f"{ROOT}/hypermapper_logfile.log") as hm_file:
            for line in hm_file.readlines():
                if symbol in line:
                    feat_imps = line[
                        line.find(symbol) + len(symbol) : line.rfind("]") + 1
                    ]
                    with open(f"{simple_file_name}_{run_ind}.csv", "a") as custom_file:
                        custom_file.write("\n" + feat_imps)
        subprocess.run("sudo rm hypermapper_logfile.log", shell=True)


def run_hypermapper_from_configs(
    config_csv_file_path, simple_file_name="simple_test", file_name="test"
):
    """
    Runs hypermapper that repeats the configurations specificed by a previous run
    """
    config_index = 0

    def run_benchmark(knobs, config_index):
        options = {
            "output_file": f"{simple_file_name}.csv",
            "readwritepercent": 50,
            "threads": 32,
        }
        # knobs are input from hypermapper optimizer - but ignore and change them since we are going to get them from a file for RUN_1
        df = pd.read_csv(config_csv_file_path, sep=",")
        knob_configs = df[config.INPUT_PARAMETERS]
        knobs = knob_configs.iloc[config_index].to_dict()
        if config_index == 100:
            config_index = 0
        else:
            config_index += 1
        throughput = run_benchmark(knobs, options, file_name)
        return -int(throughput)

    subprocess.run("python setup_optimizer_config.py", shell=True)
    optimizer.optimize(
        "util/optimizer_scenario.json", run_benchmark, args=(config_index)
    )


def run_manual(simple_file_name="simple_test", file_name="test"):
    options = {
        "output_file": f"{simple_file_name}.csv",
        # 'testing': True,
        "readwritepercent": 50,
        "threads": 32,
    }

    knob_tests = [
        {
            "block_size": "4096",
            "cache_index_and_filter_blocks": "false",
            "compaction_readahead_size": "0",
            "compression_type": "snappy",
            "level0_file_num_compaction_trigger": "4",
            "level0_slowdown_writes_trigger": "0",
            "level0_stop_writes_trigger": "32",
            "max_background_compactions": "1",
            "max_background_flushes": "1",
            "max_bytes_for_level_multiplier": "10",
            "write_buffer_size": "67108864",
        },
    ]
    for knobs in knob_tests:
        tps = run_benchmark(knobs, options, file_name)
        print(tps)
