#!/bin/bash

while true
do
    curl -kv -w '\n* Response time: %{time_total}s\n' $1
    sleep ${2:-0.5}
done
