#!/bin/bash

set -e
set -o pipefail

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd ..

: ${NEO4J_CONTAINER_ROOT:?"Environment variable NEO4J_CONTAINER_ROOT is unset or empty"}
: ${NEO4J_DATA_DIR:?"Environment variable NEO4J_DATA_DIR is unset or empty"}
: ${NEO4J_VERSION:?"Environment variable NEO4J_VERSION is unset or empty"}
: ${NEO4J_CONTAINER_NAME:?"Environment variable NEO4J_CONTAINER_NAME is unset or empty"}

if [ ! -d ${NEO4J_DATA_DIR} ]; then
    echo "Neo4j data directory does not exist"
    exit 1
fi

docker run --rm \
    --user="$(id -u):$(id -g)" \
    --publish=7474:7474 \
    --publish=7687:7687 \
    --detach \
    ${NEO4J_ENV_VARS} \
    --volume=${NEO4J_DATA_DIR}:/data \
    --volume=${NEO4J_CONTAINER_ROOT}/logs:/logs \
    --volume=${NEO4J_CONTAINER_ROOT}/import:/var/lib/neo4j/import \
    --volume=${NEO4J_CONTAINER_ROOT}/plugins:/plugins \
    --volume=${NEO4J_CONTAINER_ROOT}/conf:/conf \
    --env NEO4JLABS_PLUGINS='["apoc", "graph-data-science"]' \
    --env NEO4J_AUTH=none \
    --name ${NEO4J_CONTAINER_NAME} \
    neo4j:${NEO4J_VERSION}

# docker run --rm \
#     --user="$(id -u):$(id -g)" \
#     --publish=7474:7474 \
#     --publish=7687:7687 \
#     --detach \
#     ${NEO4J_ENV_VARS} \
#     --volume=${NEO4J_DATA_DIR}:/data \
#     --volume=${NEO4J_CONTAINER_ROOT}/logs:/logs \
#     --volume=${NEO4J_CONTAINER_ROOT}/import:/var/lib/neo4j/import \
#     --volume=${NEO4J_CONTAINER_ROOT}/plugins:/plugins \
#     --volume=${NEO4J_CONTAINER_ROOT}/conf:/conf \
#     --env NEO4JLABS_PLUGINS='["apoc", "graph-data-science"]' \
#     --env NEO4J_AUTH=none \
#     --env NEO4J_dbms_default__listen__address=0.0.0.0 \
#     --env NEO4J_dbms_memory_heap_max__size=5GB \
#     --env NEO4J_dbms_memory_pagecache_size=256M \
#     --env NEO4J_dbms_checkpoint_interval_time=1h \
#     --env NEO4J_dbms_tx__state_memory__allocation=OFF_HEAP \
#     --env NEO4J_dbms_memory_off__heap_max__size= \
#     --name ${NEO4J_CONTAINER_NAME} \
#     neo4j:${NEO4J_VERSION}

echo "Waiting for the database to start..."
until docker exec --interactive --tty ${NEO4J_CONTAINER_NAME} cypher-shell "RETURN 'Database has started successfully' AS message"; do
    sleep 1
done
