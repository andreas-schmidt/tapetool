from __future__ import print_function

from tapetool.helpers import read_wav, db, rms
from tapetool.analysis import timeslice, mol_1k, find_mol

fs, data = read_wav("05-1905.wav")
data_volramp = data[58*fs+1000:68*fs]
dt = 0.05

with open('mol.dat', 'w') as out:
    t, lvl, thd = mol_1k(fs, data_volramp, dt)
    print("MOL 3%:", round(find_mol(lvl, thd), 1))
    print("MOL 1%:", round(find_mol(lvl, thd, 1.), 1))
    for i in zip(t, lvl, thd):
        print(*i, file=out)

