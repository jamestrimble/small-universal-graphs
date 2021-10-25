#!/bin/bash

set -euf -o pipefail

filename=$1
type=$2
nP=$3

awk -f adjmat_to_dimacs.awk < $filename > target.dimacs 
rm -f results.txt
cat ../graphs/${type}${nP}.g6 | while read -r P; do
    echo $P | ../showg -e > pattern.txt
    awk -f to_dimacs_format.awk < pattern.txt > pattern.dimacs
    ./glasgow_subgraph_solver --induced --format dimacs pattern.dimacs target.dimacs | grep 'status =' >> results.txt
done

cat results.txt | sort | uniq -c
