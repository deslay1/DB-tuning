# Preparations for benchmarking on Linux
Installation stuff
```
sudo apt update
sudo apt upgrade
sudo apt install build-essential devscripts default-jre default-jdk git maven
```
Also remember to set a JAVA_HOME environment variable in */etc/environment* that points to the java jdk path. 

## Compiling RocksDB (not necessary for benchmarking)
Just clone the github repository and follow the steps provided in INSTALL.md. Although the installation steps do not specifically mention Ubuntu you can follow the Debian steps and it should work. Then just run
```
make static_lib
```
in the root directory of the repository. This is will create a librocksdb.a file that can then be used in a project.

For RocksDBJava, run:
```
make rocksdbjava
```
which should provide a .jni file in *java/target/*.

## Benchmarking with YCSB (Providing an optionsfile)

Follow the download command from the main page of the github repository, NOT in the rocksdb subdirectory, since it will give you errors later. Afterwards you can run the commands that you want directly. For workload A, we would do the following:
Load data:
```
bin/ycsb.sh load rocksdb -s -P workloads/workloada -p rocksdb.dir=<path_to_database_directory> -p rocksdb.optionsfile=<path_to_options_file>
```
Run:
```
bin/ycsb.sh run rocksdb -s -P workloads/workloada -p rocksdb.dir=<path_to_database_directory> -p rocksdb.optionsfile=<path_to_options_file>
```
Note that the options file is optional. If it is not provided it will just use its default options that can be identified by the file in the created database directory.

The results are automatically printed out in the command line.

## BEST: Benchmarkning with RocksDB tool *db_bench* (options file or command line flags)
First install the necessary tools with `sudo apt install rocksdb-tools`.

Example *memory workload performance* commands to fill up a database instance and run a benchmark can be found at https://github.com/facebook/rocksdb/wiki/RocksDB-In-Memory-Workload-Performance-Benchmarks

For what type of benchmarks and workloads you can run see either a list at https://github.com/facebook/rocksdb/wiki/Benchmarking-tools or run `db_bench --help`.


## Using an editor to edit and save remote files via ssh
By default, we do not have root privileges so we cannot just edit files outside of the command line however we want.
A workaround is for every single file to transfer ownership from root to your own user and then transfer it back when you are done:
```
sudo chown <myuser> /path/to/file
code /path/to/file
sudo chown root /path/to/file
```