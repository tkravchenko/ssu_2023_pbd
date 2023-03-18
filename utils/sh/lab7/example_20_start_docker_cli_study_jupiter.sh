#!/usr/bin/env bash

set -u;
#set -x;

docker build -t study_bd_jupyter:latest -f Dockerfile.study_bd_jupyter .
docker run --rm --name study_bd_jupyter  -p 8888:8888 -v $PWD:/app study_bd_jupyter:latest
