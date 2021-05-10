Configure the program you want to run in run_optimizer.py first and then proceed.

## 1. Script running in background
Cofirm config options in files such as config.py and then run the script background.sh script by doing the following:
```
chmod +x background.sh
nohup ./background.sh > /dev/null 2>&1&
```
The last part of the nohup command is to ignore output that is automatically saved to nohup.out (since we will reach file size limit during testing)


## Useful commands
To check if scripts are active, use
```
ps aux | grep background
```  
To kill a process, run 
``` 
kill -9 <id of process>
``` 