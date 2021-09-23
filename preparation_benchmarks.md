# Preparing for Neo4j benchmark
Create the following structure
* ldbc
  * ldbc_snb_datagen_hadoop
  * ldbc_snv_driver
  * ldbc_snb_interactive

By cloning the repositories:
```
git clone https://github.com/ldbc/ldbc_snb_interactive
``` 
``` 
git clone --branch 0.3.5 https://github.com/ldbc/ldbc_snb_driver
```
``` 
git clone https://github.com/ldbc/ldbc_snb_datagen_hadoop
``` 

According to the driver, you need Java 8 and maven, so:
``` 
sudo apt install openjdk-8-jdk openjdk-8-jre maven
``` 
We also need Docker19+: https://docs.docker.com/engine/install/ubuntu/


Then follow the guides in the interactive repository followed by the instructions in the \<repo\>/cypher.