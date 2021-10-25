#!/bin/bash

set -euf -o pipefail

type=$1
nP=$2
nT=$3

cat ../graphs/graph${nT}.g6 | while read -r T; do
    echo $T | ../showg -e > target.txt
    awk -f to_dimacs_format.awk < target.txt > target.dimacs
    rm -f results.txt
    cat ../graphs/${type}${nP}.g6 | while read -r P; do
        echo $P | ../showg -e > pattern.txt
        awk -f to_dimacs_format.awk < pattern.txt > pattern.dimacs
        ./glasgow_subgraph_solver --induced --format dimacs pattern.dimacs target.dimacs | grep 'status =' >> results.txt
    done

    if ! grep -q 'false' results.txt; then
        echo $T
    fi
done
