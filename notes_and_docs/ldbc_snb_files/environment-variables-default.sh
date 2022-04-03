cd "$( cd "$( dirname "${BASH_SOURCE[0]:-${(%):-%x}}" )" >/dev/null 2>&1 && pwd )"
cd ..

export NEO4J_CONTAINER_ROOT=`pwd`/scratch
export NEO4J_DATA_DIR=${NEO4J_CONTAINER_ROOT}/data
export NEO4J_VERSION=4.3.4
export NEO4J_ENV_VARS=""
# export NEO4J_VANILLA_CSV_DIR=`pwd`/test-data/vanilla
# export NEO4J_CONVERTED_CSV_DIR=`pwd`/test-data/converted
export NEO4J_VANILLA_CSV_DIR=~/ldbc/ldbc_snb_datagen_hadoop/social_network
export NEO4J_CONVERTED_CSV_DIR=~/ldbc/ldbc_snb_datagen_hadoop/converted
export NEO4J_CSV_POSTFIX=_0_0.csv
export NEO4J_CONTAINER_NAME=snb-interactive-neo4j
