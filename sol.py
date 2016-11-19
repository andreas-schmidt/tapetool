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
    # cut the right part of the audio file
    ramp = data[t0 * fs:(t0 + 5) * fs]

    # calculate the curve
    x, y = sol(fs, ramp, 0.1)

    # find and print the maximum
    i = np.argmax(y)
    print "%10s: %5.1fdB at %.1fs" % (label[t0], round(y[i], 1), x[i])

    # store data
    if not columns:
        columns.append(x)
    columns.append(y)

# save results
np.savetxt('sol.dat', np.transpose(columns), fmt='%-10.6g')

