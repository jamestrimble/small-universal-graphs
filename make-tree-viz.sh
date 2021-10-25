#!/bin/bash

set -eu -o pipefail

python3 find_universal_graphs_heur_for_trees-with-viz.py 7 11 10000 1 1
dot tmp/tree.dot | grep -v '\[' | grep pos | sed 's/[^"]*"//' | sed 's/".*//' > tmp/tree.txt
python3 find_universal_graphs_heur_for_trees-with-viz.py 7 11 10000 1 2 > paper/img/tree-example.tex
