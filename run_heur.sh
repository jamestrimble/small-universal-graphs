#!/bin/bash

time pypy3 find_universal_graphs_heur.py 6 14 1000 1 | tee heur-graphs/graph6-14.txt
time pypy3 find_universal_graphs_heur.py 7 18 10000 1 | tee heur-graphs/graph7-18.txt

time pypy3 find_universal_graphs_heur_for_trees.py 7 11 1000 1 | tee heur-graphs/tree7-11.txt
time pypy3 find_universal_graphs_heur_for_trees.py 8 13 10000 1 | tee heur-graphs/tree9-13.txt
time pypy3 find_universal_graphs_heur_for_trees.py 9 15 10000 1 | tee heur-graphs/tree11-15.txt
time pypy3 find_universal_graphs_heur_for_trees.py 10 18 10000 1 | tee heur-graphs/tree12-18.txt
