from __future__ import print_function

from tapetool.helpers import read_wav, db, rms
from tapetool.analysis import it_timeslice
from tapetool.filters import thd_for_1k

fs, data = read_wav("05-1905.wav")

reflevel = data[16*fs:26*fs]
thd_rl = 100. * rms(thd_for_1k(fs, reflevel)) / rms(reflevel) 
print("THD at reference level:", thd_rl)

ramp = data[58*fs:68*fs]
sig = list(it_timeslice(fs, ramp))
thd = list(it_timeslice(fs, thd_for_1k(fs, ramp)))

rl = db(rms(reflevel))
out = open('mol.dat', 'w')
for a, b in zip(sig, thd):
    i, t, l1 = a
    _, _, l2 = b
    x = db(l1) - rl
    k = 100. * l2 / l1
    print(*(t, ) + tuple(x) + tuple(k), file=out)
