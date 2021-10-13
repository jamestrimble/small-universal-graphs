# vim: set et ft=gnuplot sw=4 :

set terminal tikz standalone color size 7cm,5cm font '\small' preamble '\usepackage{times,microtype,algorithm2e,algpseudocode,amssymb}'
set output "deg-scatter.tex"
#set terminal png
#set output "bounds-plot.png"

set xlabel '$\big|{2|E(G)| - {|V(G)| \choose 2}}\big|$'
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

plot "results.txt" u 2:3 pt 7 lc rgb "#991f77b4" ps .6 notitle
