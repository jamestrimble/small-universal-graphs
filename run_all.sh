#!/bin/bash

set -eu -o pipefail

rm -rf results
mkdir results

cat exhaustive_tests.txt | while read type p t; do
    echo $type $p $t
    python3 find_universal_graphs.py $type $p $t --check > results/$type-$p-$t.txt
    python3 graph6_to_dot.py results/$type-$p-$t.txt dot-graphs/$type-$p-$t-{}.dot
done
