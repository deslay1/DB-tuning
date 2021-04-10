@ECHO OFF
>output.txt (
    C:\\dev\\YCSB\\bin\\ycsb.bat load rocksdb -s -P C:\\dev\\YCSB\\workloads\\workloada -p rocksdb.dir=C:\\rocksdb_test -p rocksdb.optionsfile=C:\\dev\\YCSB\\rocksdb\\full_options.ini
    C:\\dev\\YCSB\\bin\\ycsb.bat run rocksdb -s -P C:\\dev\\YCSB\\workloads\\workloada -p rocksdb.dir=C:\\rocksdb_test -p rocksdb.optionsfile=C:\\dev\\YCSB\\rocksdb\\full_options.ini
)
PAUSE
