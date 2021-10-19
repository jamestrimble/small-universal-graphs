# vim: set et ft=gnuplot sw=4 :

set terminal tikz standalone color size 8cm,5.5cm font '\scriptsize' preamble '\usepackage{times,microtype,algorithm2e,algpseudocode,amssymb}'
set output "second-experiment-plot.tex"
#set terminal png
#set output "bounds-plot.png"

set xlabel 'Ordering strategy'
set ylabel 'Number of calls, thousands'
set border 3
set grid x y front
set xtics nomirror
set ytics nomirror
set tics front
#set size square
set xrange [.5:4.5]
set xtics ("Automorphisms" 1, "Edges" 2, "Almost random" 3, "Random" 4)
set yrange [0:]
#set ytics 0,.5,2.5
#set format x '$10^{%T}$'
#set format y '$10^{%T}$'

plot \
    "results-of-second-experiment_graph.tsv" u 5:($3/1000) pt 7 lc rgb "#991f77b4" ps .3 notitle, \
    "results-of-second-experiment-summary_graph.tsv" using ($1-.2):($2/1000):(.4):(0) with vectors nohead lw 1 lc rgb "#000000" notitle
