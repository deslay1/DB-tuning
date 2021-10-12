#!/bin/bash

set -e
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

echo ===============================================================================
echo Loading the Neo4j database with the following parameters
echo -------------------------------------------------------------------------------
echo NEO4J_CONTAINER_ROOT: ${NEO4J_CONTAINER_ROOT}
echo NEO4J_DATA_DIR: ${NEO4J_DATA_DIR}
echo NEO4J_VANILLA_CSV_DIR: ${NEO4J_VANILLA_CSV_DIR}
echo NEO4J_CONVERTED_CSV_DIR: ${NEO4J_CONVERTED_CSV_DIR}
echo NEO4J_CSV_POSTFIX: ${NEO4J_CSV_POSTFIX}
echo NEO4J_VERSION: ${NEO4J_VERSION}
echo NEO4J_CONTAINER_NAME: ${NEO4J_CONTAINER_NAME}
echo NEO4J_ENV_VARS: ${NEO4J_ENV_VARS}
echo ===============================================================================

: ${NEO4J_CONTAINER_ROOT:?"Environment variable NEO4J_CONTAINER_ROOT is unset or empty"}
: ${NEO4J_DATA_DIR:?"Environment variable NEO4J_DATA_DIR is unset or empty"}
: ${NEO4J_VANILLA_CSV_DIR:?"Environment variable NEO4J_VANILLA_CSV_DIR is unset or empty"}
: ${NEO4J_CONVERTED_CSV_DIR:?"Environment variable NEO4J_CONVERTED_CSV_DIR is unset or empty"}
: ${NEO4J_CSV_POSTFIX:?"Environment variable NEO4J_CSV_POSTFIX is unset or empty"}
: ${NEO4J_VERSION:?"Environment variable NEO4J_VERSION is unset or empty"}
: ${NEO4J_CONTAINER_NAME:?"Environment variable NEO4J_CONTAINER_NAME is unset or empty"}
# ${NEO4J_ENV_VARS} can be empty, hence no check is required

./stop-neo4j.sh

# copy  over snapshot
# rm -r ${NEO4J_CONTAINER_ROOT}/data
# mkdir ${NEO4J_CONTAINER_ROOT}/data
# cp -r ${NEO4J_CONTAINER_ROOT}/../backup_data ${NEO4J_CONTAINER_ROOT}/data
rsync -av ${NEO4J_CONTAINER_ROOT}/../backup_databases/ ${NEO4J_CONTAINER_ROOT}/data/databases

./start-neo4j.sh
./create-indices.sh
