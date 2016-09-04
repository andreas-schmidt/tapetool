#!/usr/bin/gnuplot -persist

set title "{title}"
set xlabel "Wellenzahl / 1/m"
set ylabel "Pegel hinter Band / dB"

set grid
set style data fsteps
set yrange [-25:-15]

phi_w(x, b) = 1. - 0.2 * cos(pi*b*x + 1./6) / (b*x)**(2./3)
f(x, b, c) = 20 * log10(phi_w(x, b)) + c

b = 700.
c = -20.
#fit [400:] f(x, 1./b, c) '{prefix}-1905.dat' u 2:{col} via b, c

plot '{prefix}-1905.dat' u 2:{col} t '19.05 cm/s', \
     '{prefix}-0953.dat' u 2:{col} t '9.53 cm/s', \
     '{prefix}-0476.dat' u 2:{col} t '4.76 cm/s'#, \
#    f(x, 1./b, c) w l lw 2 lc 0 t sprintf("%.2f/m", b)

