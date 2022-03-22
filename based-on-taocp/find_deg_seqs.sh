#!/bin/bash

set -eu -o pipefail

rm -rf degree-sequences
mkdir degree-sequences
rm -rf degree-sequences-summary
mkdir degree-sequences-summary
rm -rf degree-sequences-example-graphs
mkdir degree-sequences-example-graphs

cat ../exhaustive_tests.txt | while read type p t; do
    echo $type $p $t
    python3 graph6_to_degree_sequences.py ../results/$type-$p-$t.txt > degree-sequences/$type-$p-$t.txt
    python3 deg_seqs_summary.py < degree-sequences/$type-$p-$t.txt > degree-sequences-summary/$type-$p-$t.txt
    python3 deg_seqs_summary_table.py $p $t < degree-sequences/$type-$p-$t.txt > degree-sequences-summary/$type-$p-$t.tex
    python3 ../graph6_to_dot.py <(cut -d' ' -f1 degree-sequences-summary/$type-$p-$t.txt) 'degree-sequences-example-graphs/'$type-$p-$t-'{}.txt'
    count=$(wc -l < degree-sequences-summary/$type-$p-$t.txt)
    for i in $(seq 0 $((count - 1))); do
        neato degree-sequences-example-graphs/$type-$p-$t-$i.txt -Tpdf -o degree-sequences-example-graphs/$type-$p-$t-$i.pdf -Nwidth=.12 -Gmargin=0.003 -Gsplines=true
    done
done
