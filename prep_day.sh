#!/bin/bash

read -p "enter two-digit-day, e.g. 09 or 15: " day

mkdir python/src/$day
touch python/src/$day/solution.py
touch python/src/$day/input_sample.txt
touch python/src/$day/input.txt

url=https://adventofcode.com/2023/day/$day

echo "\"\"\"${url}\"\"\"" >> python/src/$day/solution.py