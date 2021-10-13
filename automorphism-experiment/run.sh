#!/bin/bash

set -eu -o pipefail

(
cd ..
time pypy3 find_universal_graphs.py graph 5 8 --automorphism-stats | tee automorphism-experiment/results.txt
)
