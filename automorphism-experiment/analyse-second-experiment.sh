#!/bin/bash

set -eu -o pipefail

#echo "Results for automorphism and degree pattern orders:"
#cat results-of-second-experiment.txt
#echo
for type in graph sample-of-graphs; do
    echo "Results for "automorphisms" pattern order:"
    cat results-of-second-experiment_automorphisms_$type.txt | cut -d' ' -f1 | \
        datamash --header-out min 1 max 1 mean 1 | column -t
    echo
    echo "Results for "degree" pattern order:"
    cat results-of-second-experiment_degree_$type.txt | cut -d' ' -f1 | \
        datamash --header-out min 1 max 1 mean 1 | column -t
    echo
    echo "Results for random pattern order:"
    cat results-of-second-experiment_random_$type.txt | cut -d' ' -f1 | \
        datamash --header-out min 1 max 1 mean 1 | column -t
    echo
    echo "Results for almost-random pattern order:"
    cat results-of-second-experiment_almost-random_$type.txt | cut -d' ' -f1 | \
        datamash --header-out min 1 max 1 mean 1 | column -t
    echo
    echo
done

Rscript reshape.R

gnuplot second-experiment-scatter.gnuplot
latexmk -pdf second-experiment-plot

gnuplot second-experiment-scatter-using-sample.gnuplot
latexmk -pdf second-experiment-plot-using-sample
