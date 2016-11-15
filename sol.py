from __future__ import print_function

import numpy as np
from tapetool.helpers import read_wav
from tapetool.analysis import sol

fs, data = read_wav("05-1905.wav")

label = {
    78: '6.3 kHz',
    83: '10 kHz',
    88: '12.5 kHz',
    93: '14 kHz',
    98: '16 kHz',
}

columns = list()
for t0, l in sorted(label.items()):
    ramp = data[t0 * fs:(t0 + 5) * fs]
    m, x, y = sol(fs, ramp, 0.1)
    if not columns:
        columns.append(x)
    columns.append(y)
    print("%10s %5.1f" % (label[t0], round(m, 1)))

out = open('sol.dat', 'w')
for row in zip(*columns):
    print(*row, file=out)

