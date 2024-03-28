#! /usr/bin/env bash

for i in {2..5}
do
    curl -w "\n" http://192.168.56.$i:8080/hello/john
done