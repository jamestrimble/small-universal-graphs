# vim: set et ft=gnuplot sw=4 :

set terminal tikz standalone color size 7cm,5cm font '\small' preamble '\usepackage{times,microtype,algorithm2e,algpseudocode,amssymb}'
set output "automorphisms-scatter.tex"
#set terminal png
#set output "bounds-plot.png"

set xlabel 'Size of automorphism group of $G$'
set ylabel 'Number of graphs containing $G$'
set border 3
set grid x y front
set xtics nomirror
set ytics nomirror
set tics front
set logscale
#set size square
#set xrange [1:200]
###set xtics 0,5,20
###set yrange [0:2.5]
###set ytics 0,.5,2.5
#set format x '$10^{%T}$'
#set format y '$10^{%T}$'

plot "results.txt" u 1:3 pt 7 lc rgb "#991f77b4" ps .6 notitle
