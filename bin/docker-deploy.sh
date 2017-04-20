#!/bin/bash

cd $(dirname $0)/..

docker stack deploy --compose-file=docker-compose.yaml tinypaste