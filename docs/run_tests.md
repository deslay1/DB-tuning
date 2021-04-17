Configure the program you want to run in run_optimizer.py first and then proceed.

## 1. internal tool db_bench
If you configured testing for this tool, run the script background_1.sh script by doing the following:
```
chmod +x background_1.sh
nohup ./background_1.sh > /dev/null 2>&1&
```
The last part of the nohup command is to ignore output that is automatically saved to nohup.out (since we will reach file size limit during testing)

## 2. YCSB
If you configured testing for YCSB, first change the *rm -r* path given in background_2.sh to the db_dir_path for YCSB as in config.py.

Then run the script background_2.sh script by doing the following:
```
chmod +x background_2.sh
nohup ./background_2.sh > /dev/null 2>&1&
```

## Useful commands
To check if scripts are active, use `ps aux | grep background`  
To kill a process, run `kill -9 <id of process>`