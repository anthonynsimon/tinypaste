#!/bin/bash

cd $(dirname $0)

docker build --rm -t tinypaste/logstash ../logstash
docker build --rm -t pastes-api ../pastes-api
docker build --rm -t shorten-id-api ../shorten-id-api