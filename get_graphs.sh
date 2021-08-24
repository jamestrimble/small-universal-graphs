#!/bin/bash

set -eu -o pipefail

cd graphs

# Copy trees with 1-3 vertices
cp ../extra-graphs/* .

# Get McKay's lists of trees
for i in $(seq 4 12); do
    wget https://users.cecs.anu.edu.au/~bdm/data/tree$i.all.tar.gz; tar xvf tree$i.all.tar.gz
    cat tree$i.*.txt > tree$i.all.txt
done

# Get McKay's lists of graphs
for i in $(seq 1 9); do
    wget https://users.cecs.anu.edu.au/~bdm/data/graph$i.g6
done
wget https://users.cecs.anu.edu.au/~bdm/data/graph10.g6.gz
gunzip graph10.g6.gz
