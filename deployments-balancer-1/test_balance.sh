#! /usr/bin/env bash

for i in {1..5}
do
    curl -Is http://192.168.56.2/ |grep -i Cookie
done
