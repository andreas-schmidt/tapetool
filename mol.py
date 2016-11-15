from __future__ import print_function

from tapetool.helpers import read_wav, db, rms
from tapetool.analysis import timeslice
from tapetool.filters import thd_for_1k

fs, data = read_wav("05-1905.wav")

reflevel = data[16*fs:26*fs]
thd_rl = 100. * rms(thd_for_1k(fs, reflevel)) / rms(reflevel) 
print("THD at reference level:", thd_rl)

ramp = data[58*fs:68*fs]
sig_x, sig_y = timeslice(fs, ramp, 0.05)
_, thd_y = timeslice(fs, thd_for_1k(fs, ramp), 0.05)

rl = db(rms(reflevel))
with open('mol.dat', 'w') as out:
    for t, a, b in zip(sig_x, sig_y, thd_y):
        print(t, db(a) - rl[0], 100. * b / a, file=out)
