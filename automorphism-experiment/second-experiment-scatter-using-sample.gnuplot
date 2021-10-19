# vim: set et ft=gnuplot sw=4 :

set terminal tikz standalone color size 8cm,5.5cm font '\scriptsize' preamble '\usepackage{times,microtype,algorithm2e,algpseudocode,amssymb}'
set output "second-experiment-plot-using-sample.tex"
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
set xtics ("Automorphisms" 1, "Degree" 2, "Almost random" 3, "Random" 4)
set yrange [0:]
#set ytics 0,.5,2.5
#set format x '$10^{%T}$'
#set format y '$10^{%T}$'

plot \
"< awk 'NR==1 || $1==1' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==2' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==3' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==4' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==5' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==6' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==7' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==8' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==9' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==10' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==11' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==12' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==13' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==14' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==15' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==16' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==17' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==18' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==19' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==20' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==21' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==22' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==23' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==24' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==25' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==26' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==27' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==28' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==29' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==30' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==31' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==32' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==33' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==34' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==35' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==36' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==37' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==38' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==39' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==40' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==41' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==42' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==43' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==44' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==45' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==46' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==47' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==48' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==49' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
"< awk 'NR==1 || $1==50' results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) w l lc rgb "#aa1f77b4" lw .3 notitle, \
    "results-of-second-experiment_sample-of-graphs.tsv" u 5:($3/1000) pt 7 lc rgb "#991f77b4" ps .3 notitle, \
    "results-of-second-experiment-summary_sample-of-graphs.tsv" using ($1-.2):($2/1000):(.4):(0) with vectors nohead lw 1 lc rgb "#000000" notitle
