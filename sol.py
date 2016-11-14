from __future__ import print_function

from tapetool.helpers import read_wav, db, rms, timeslice

fs, data = read_wav("05-1905.wav")

reflevel = db(rms(data[16*fs:26*fs]))
ramps = [data[i*fs:(i+5)*fs] for i in range(78, 103, 5)]
alldat = [list(timeslice(fs, i, 0.05)) for i in ramps]

out = open('sol.dat', 'w')
for allcol in zip(*alldat):
    t = allcol[0][1]
    val = [db(i[2][0]) for i in allcol]
    print(t, *val, file=out)

