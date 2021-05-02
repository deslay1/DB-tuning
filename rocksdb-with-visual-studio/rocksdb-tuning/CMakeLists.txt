# CMakeList.txt : CMake project for rocksdb-tuning, include source and define
# project specific logic here.
#
cmake_minimum_required (VERSION 3.8)

project ("rocksdb-tuning")

# Add source to this project's executable.
add_executable (rocksdb-tuning "rocksdb-tuning.cpp" "rocksdb-tuning.h")

# RocksDB
find_package(RocksDB CONFIG REQUIRED)
target_link_libraries(rocksdb-tuning PRIVATE RocksDB::rocksdb)

# For JSON-parsing
find_package(nlohmann_json CONFIG REQUIRED)
target_link_libraries(rocksdb-tuning PRIVATE nlohmann_json nlohmann_json::nlohmann_json)

#include_directories(${CMAKE_SOURCE_DIR}/config.json)
