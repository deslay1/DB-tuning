# Database tuning project
I used an Anaconda environment with Python3.8. The dependencies are in the **requirements.txt** file. To replicate the environment, you can just run:

```conda create --name <envname> --file requirements.txt```

---
Running `python setup_optimizer_config.py` will create the the json file(s) that are needed for hypermapper. The benchmark program is located in **run_hypermapper.py** and can be run using `python run_optimizer.py`. The benchmark class for RocksDB is defined in **benchmark.py**

