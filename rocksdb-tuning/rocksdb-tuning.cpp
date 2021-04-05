#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>

#include "rocksdb-tuning.h"

#include "rocksdb/db.h"
#include "rocksdb/slice.h"
#include "rocksdb/options.h"
#include "nlohmann/json.hpp"

//using namespace std; // One can change all std::string to string for example
using namespace ROCKSDB_NAMESPACE;

// for convenience
using json = nlohmann::json;

// #if defined(OS_WIN)
// std::string kDBPath = "C:\\Windows\\TEMP\\rocksdb_simple_example";
// #else
// std::string kDBPath = "/tmp/rocksdb_simple_example";
// #endif

std::string kDBPath = "C:\\rocksdb_test";

int main()
{
    DB* db;
    Options options;

    // Read from config file
    std::ifstream file("D:/ProgProjects/RocksDB-tuning/rocksdb-tuning/config.json");
    json j;
    try {
        j = json::parse(file);
    }
    catch (json::parse_error& e)
    {
        std::cerr << e.what() << std::endl;
    }
    // Loop through options
    for (auto& opt : j.items()) {
        if (opt.key() == "bytes_per_sync") {
            options.bytes_per_sync = opt.value();
        }
        else if (opt.key() == "compaction_readahead_size") {
            options.compaction_readahead_size = opt.value();
        }
        // grab other options too....
    }

    // Optimize RocksDB. This is the easiest way to get RocksDB to perform well
    options.IncreaseParallelism();
    options.OptimizeLevelStyleCompaction();
    // create the DB if it's not already present
    options.create_if_missing = true;

    // Destroy existing
    Status s = DestroyDB(kDBPath, options);
    assert(s.ok());
    // open DB
    s = DB::Open(options, kDBPath, &db);
    assert(s.ok());


    // BELOW: Operations are performed and asserted. Perhaps not useful for my use case.

    // Put key-value
    s = db->Put(WriteOptions(), "key1", "value");
    assert(s.ok());
    std::string value;
    // get value
    s = db->Get(ReadOptions(), "key1", &value);
    assert(s.ok());
    assert(value == "value");

    // atomically apply a set of updates
    {
        WriteBatch batch;
        batch.Delete("key1");
        batch.Put("key2", value);
        s = db->Write(WriteOptions(), &batch);
    }

    s = db->Get(ReadOptions(), "key1", &value);
    assert(s.IsNotFound());

    db->Get(ReadOptions(), "key2", &value);
    assert(value == "value");

    {
        PinnableSlice pinnable_val;
        db->Get(ReadOptions(), db->DefaultColumnFamily(), "key2", &pinnable_val);
        assert(pinnable_val == "value");
    }

    {
        std::string string_val;
        // If it cannot pin the value, it copies the value to its internal buffer.
        // The intenral buffer could be set during construction.
        PinnableSlice pinnable_val(&string_val);
        db->Get(ReadOptions(), db->DefaultColumnFamily(), "key2", &pinnable_val);
        assert(pinnable_val == "value");
        // If the value is not pinned, the internal buffer must have the value.
        assert(pinnable_val.IsPinned() || string_val == "value");
    }

    PinnableSlice pinnable_val;
    s = db->Get(ReadOptions(), db->DefaultColumnFamily(), "key1", &pinnable_val);
    assert(s.IsNotFound());
    // Reset PinnableSlice after each use and before each reuse
    pinnable_val.Reset();
    db->Get(ReadOptions(), db->DefaultColumnFamily(), "key2", &pinnable_val);
    assert(pinnable_val == "value");
    pinnable_val.Reset();
    // The Slice pointed by pinnable_val is not valid after this point

    delete db;

    return 0;
}
