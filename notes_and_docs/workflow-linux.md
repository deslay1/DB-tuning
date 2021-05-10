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


## BEST: Benchmarking with RocksDB tool *db_bench* (by providing options file or command line flags)

In the main rocksdb folder (of repository) I ran `make release`, which is perhaps unnecessary.
To compile the tools, run `make tools`

Then you can run `./db_bench` command (again from the main directory)

If problems occur, see first the Install file in the RocksDB repository on github.

### [OLD] 
{

I had problems getting this to work on Ubuntu.
Running `make all` in the main directory wasn't useful. First of you have to check that gflags is installed. I then added the following paths to my */etc/environment* file.
```
CPATH="/usr/include/gflags/"
LIBRARY_PATH="/usr/local/lib"
```
}
### Suboptimal alternative: With apt package (uses DB version 5.17, i.e. an old version)
First install the necessary tools with `sudo apt install rocksdb-tools`.

Example *memory workload performance* commands to fill up a database instance and run a benchmark can be found at https://github.com/facebook/rocksdb/wiki/RocksDB-In-Memory-Workload-Performance-Benchmarks

For what type of benchmarks and workloads you can run see either a list at https://github.com/facebook/rocksdb/wiki/Benchmarking-tools or run `db_bench --help`.


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


## Using vscode to edit and save remote files via ssh
By default, we do not have root privileges so we cannot just edit files outside of the command line however we want.
A workaround is to transfer ownership from root to your own user and then transfer it back when you are done:

Folder:
```
sudo chown -R <myuser>: /path/to/folder
code /path/to/folder
sudo chown -R root: /path/to/folder
```

Single file:
```
sudo chown <myuser> /path/to/file
code /path/to/file
sudo chown root /path/to/file
```


### Commands
sudo /home/osama_eldawebi/main/rocksdb/db_bench --benchmarks="fillrandom" -num=50000000 -perf_level=3 -use_direct_io_for_flush_and_compaction=true -use_direct_reads=true -cache_size=268435456 -key_size=48 -value_size=43

sudo /home/osama_eldawebi/main/rocksdb/db_bench --benchmarks="mixgraph,stats" --use_existing_db use_direct_io_for_flush_and_compaction=true -use_direct_reads=true -cache_size=268435456 -keyrange_dist_a=14.18 -keyrange_dist_b=-2.917 -keyrange_dist_c=0.0164 -keyrange_dist_d=-0.08082 -keyrange_num=30 -value_k=0.2615 -value_sigma=25.45 -iter_k=2.517 -iter_sigma=14.236 -mix_get_ratio=0.85 -mix_put_ratio=0.14 -mix_seek_ratio=0.01 -sine_mix_rate_interval_milliseconds=5000 -sine_a=1000 -sine_b=0.000000073 -sine_d=4500000 --perf_level=1 -reads=4200000 -num=50000000 -key_size=48 --statistics=1 --duration=300


sudo /home/osama_eldawebi/main/rocksdb/sst_dump --file=./ --show_properties --command=none | grep entries | cut -c 14- | awk '{x+=$0}END{print "total number of entries: " x}'

Before filling, number of entries 37 537 707
After filling, number of entries 33 427 442
But we cap using duration...