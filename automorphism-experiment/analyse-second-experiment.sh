#!/bin/bash

set -eu -o pipefail

#echo "Results for automorphism and degree pattern orders:"
#cat results-of-second-experiment.txt
#echo
for type in graph sample-of-graphs tree; do
    echo "------------------------------"
    echo "Type:" $type
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
done | tee second-experiment-summary.txt

Rscript reshape.R

gnuplot second-experiment-scatter.gnuplot
latexmk -pdf second-experiment-plot

# Make .gnuplot file for parallel coordinates plot
cat gnuplot-parts/second-experiment-scatter-using-sample.gnuplot.START > second-experiment-scatter-using-sample.gnuplot
for run_num in $(seq 1 $(tail -n1 results-of-second-experiment_sample-of-graphs.tsv | awk '{print $1}')); do
    echo "\"< awk 'NR==1 || \$1==$run_num' results-of-second-experiment_sample-of-graphs.tsv\"" 'u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \' >> second-experiment-scatter-using-sample.gnuplot
done
cat gnuplot-parts/second-experiment-scatter-using-sample.gnuplot.END >> second-experiment-scatter-using-sample.gnuplot
gnuplot second-experiment-scatter-using-sample.gnuplot
latexmk -pdf second-experiment-plot-using-sample

gnuplot second-experiment-scatter-using-trees.gnuplot
latexmk -pdf second-experiment-plot-using-trees
