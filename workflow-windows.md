# Getting started with RocksDB on Windows
## Requirements
- At least Visual Studio 2015 update 3. So if you have 2019 that is fine.
- Visual Studio 2015 c++ Build tools (for the *zlib* library that is used by RocksDB), which can be installed as an individual component from Visual Studio, just go *Tools --> Get Tools and Features* in an open Visual Studio instance.
- CMake, https://cmake.org/
- gcc and other tools, use mingw: http://mingw-w64.org/doku.php

## Install and build RocksDB
Either:
1. Build RocksDB from source (see the github page), particularly useful is a tutorial written by someone on the wiki: https://github.com/facebook/rocksdb/wiki/Building-on-Windows

2. [WHAT I USED] Download and build with *vcpkg*, which makes the entire process easier: \
   1. Follow the steps at https://github.com/microsoft/vcpkg#quick-start-windows
   2. For CMake projects, follow the one instruction at: https://github.com/microsoft/vcpkg#vcpkg-with-visual-studio-cmake-projects
   3. If CMake is not used, then every time you build you can just link to *vcpkg* using the toolchain file as a command argument.

Basically we are going to be using Visual Studio to build this project with dependencies from *vcpkg*, which contains the RocksDB library.

## Important to configure in Visual Studio
When you create a CMake project template in Visual Studio, apart from the toolchain file according to 2.2. above, you have to add the packages you want in the *CMakeLists.txt*. For example, for RocksDB, add the following lines:
```
find_package(RocksDB CONFIG REQUIRED)
target_link_libraries(<project/main file name> PRIVATE RocksDB::rocksdb)
```
Actually, as soon as you write RocksDB in find_package, the intellisense will capture the reference and you will be able to see a short description of the package, which will also show the lines that you need to write (shown above).


# Benchmarking with YCSB

Follow the instructions at https://github.com/brianfrankcooper/YCSB/tree/master/rocksdb, but note:

- You need Maven installed and added to PATH so that you can execute *mvn*
- To start the benchmark tests you on Windows you need to use *ycsb.bat instead*, so the correponding commands for the example usage in the link are:

Loading:
```
bin\ycsb.bat load rocksdb -s -P workloads/workloada -p rocksdb.dir=<path_to_database_directory>
```

Running:
```
bin\ycsb.bat run rocksdb -s -P workloads/workloada -p rocksdb.dir=<path_to_database_directory>
```

The results are automatically printed out.