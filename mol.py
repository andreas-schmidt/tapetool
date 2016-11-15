from __future__ import print_function

from tapetool.helpers import read_wav, db, rms
from tapetool.analysis import timeslice, mol_1k
from tapetool.filters import thd_for_1k

fs, data = read_wav("05-1905.wav")
data_volramp = data[58*fs:68*fs]
dt = 0.05

with open('mol.dat', 'w') as out:
    for i in zip(*mol_1k(fs, data_volramp, dt)):
        print(*i, file=out)

