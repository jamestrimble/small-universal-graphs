#!/bin/bash

set -eu -o pipefail

iters=50
p=5
t=9

rm -f results-of-second-experiment*.txt
(
cd ..
for type in graph sample-of-graphs; do
    for i in $(seq 1 $iters); do
        echo i = $i
        time pypy3 find_universal_graphs.py --seed=$i $type $p $t >/dev/null 2>> automorphism-experiment/results-of-second-experiment_automorphisms_$type.txt
    done
    for i in $(seq 1 $iters); do
        echo i = $i
        time pypy3 find_universal_graphs.py --seed=$i $type $p $t --degree-pattern-order >/dev/null 2>> automorphism-experiment/results-of-second-experiment_degree_$type.txt
    done
    for i in $(seq 1 $iters); do
        echo i = $i
        time pypy3 find_universal_graphs.py --seed=$i $type $p $t --random-pattern-order >/dev/null 2>> automorphism-experiment/results-of-second-experiment_random_$type.txt
    done
    for i in $(seq 1 $iters); do
        echo i = $i
        time pypy3 find_universal_graphs.py --seed=$i $type $p $t --almost-random-pattern-order >/dev/null 2>> automorphism-experiment/results-of-second-experiment_almost-random_$type.txt
    done
done
)
(
cd ..
type=tree
p=6
t=8
for i in $(seq 1 $iters); do
    echo i = $i
    time pypy3 find_universal_graphs.py --seed=$i $type $p $t >/dev/null 2>> automorphism-experiment/results-of-second-experiment_automorphisms_$type.txt
done
for i in $(seq 1 $iters); do
    echo i = $i
    time pypy3 find_universal_graphs.py --seed=$i $type $p $t --degree-pattern-order >/dev/null 2>> automorphism-experiment/results-of-second-experiment_degree_$type.txt
done
for i in $(seq 1 $iters); do
    echo i = $i
    time pypy3 find_universal_graphs.py --seed=$i $type $p $t --random-pattern-order >/dev/null 2>> automorphism-experiment/results-of-second-experiment_random_$type.txt
done
for i in $(seq 1 $iters); do
    echo i = $i
    time pypy3 find_universal_graphs.py --seed=$i $type $p $t --almost-random-pattern-order >/dev/null 2>> automorphism-experiment/results-of-second-experiment_almost-random_$type.txt
done
)
