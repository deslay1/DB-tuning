# Database tuning project
I used an Anaconda environment with Python3.8. The dependencies are in the **requirements.txt** file. To replicate the environment, you can just run:

```conda create --name <envname> --file requirements.txt```

---
Running `python project/setup_optimizer_config.py` will create the the json file(s) that are needed for hypermapper. The benchmark programs are located in **project/programs** and can be imported and run in the main file using `python main.py`. The benchmark class for RocksDB is defined in **project/benchmark.py**

