#!/bin/bash

set -eu -o pipefail

gnuplot scatter.gnuplot
gnuplot deg-scatter.gnuplot
sed -i -e '19s/^\(\\path.*\)/\% \1/' *.tex # Ciaran's trick
latexmk -pdf
