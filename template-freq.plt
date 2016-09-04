#!/usr/bin/gnuplot -persist

set title "{title}"
set xlabel "Frequenz / Hz"
set ylabel "Pegel hinter Band / dB"

set grid
set style data fsteps
set xrange [20:20000]
set log x
set yrange [-30:-10]

plot 'logfreq-{prefix}-1905.dat' u 2:{col} t '19.05 cm/s', \
     'logfreq-{prefix}-0953.dat' u 2:{col} t '9.53 cm/s', \
     'logfreq-{prefix}-0476.dat' u 2:{col} t '4.76 cm/s'

