#!/bin/bash

set -eu -o pipefail

mkdir -p graphs

for i in $(seq 1 12); do
    ./nauty/gentreeg $i > graphs/tree$i.g6
done

for i in $(seq 1 10); do
    ./nauty/geng $i > graphs/graph$i.g6
done

# Copy trees with 1-3 vertices
cp extra-graphs/* graphs

cd graphs

# Get McKay's lists of trees
for i in $(seq 4 12); do
    wget https://users.cecs.anu.edu.au/~bdm/data/tree$i.all.tar.gz; tar xvf tree$i.all.tar.gz
    cat tree$i.*.txt > tree$i.all.txt
done
