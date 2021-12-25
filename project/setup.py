from project.benchmarks import RocksdbBenchmark, Neo4jBenchmark, CassandraBenchmark
from datetime import datetime
import project.configs.rocksdb_config as rocksconfig
import project.configs.neo4j_config as neoconfig
import project.configs.cassandra_config as cassconfig
import json
import os

ROOT = os.getcwd()


def setup_optimizer(
    db_parameters,
    num_samples,
    optimization_iterations,
    doe_type,
    file_name,
    resume=False,
    database="rocksdb",
):
    """
    Creates a json file for the optimizer to use.
    """

    if database == "rocksdb":
        config = rocksconfig
    elif database == "neo4j":
        config = neoconfig
    else:
        config = cassconfig

    # Update search space file
    with open(f"{ROOT}/util/search_space.json", "w") as file:
        json.dump(config.knobs, file, indent=4)

    scenario_file = f"{ROOT}/util/optimizer_scenario.json"
    scenario = {}
    scenario["application_name"] = config.APPLICATION_NAME
    scenario["optimization_objectives"] = config.OPTIMIZATION_OBJECTIVE
    scenario["optimization_iterations"] = optimization_iterations
    if resume:
        scenario["resume_optimization"] = True
        scenario["resume_optimization_data"] = f"{ROOT}/{file_name}.csv"
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
        for param in db_parameters:
            # Need to replace dots for hypermapper to validate JSON correctly. They are then put back in the benchmark class.
            valid_param = param.replace(".", "-")
            scenario["input_parameters"][valid_param] = dict(
                zip(parameter_options, [knobs[param][k] for k in parameter_options])
            )

    with open(scenario_file, "w") as sf:
        json.dump(scenario, sf, indent=4)


def run_benchmark(bench_type, knobs, options, runs=3, database="rocksdb"):
    """
    Calls the appropriate benchmark class and runs the benchmark.
    """
    if database == "rocksdb":
        bench = RocksdbBenchmark(bench_type=bench_type, options=options)
    elif database == "neo4j":
        bench = Neo4jBenchmark(bench_type=bench_type)
    else:
        bench = CassandraBenchmark(bench_type=bench_type)

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
        throughput = bench.run_benchmark(runs=runs)

    return throughput
