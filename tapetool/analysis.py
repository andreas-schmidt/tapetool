import numpy as np
from tapetool.helpers import rms, db
import tapetool.filters as filters

def it_timeslice(fs, data, dt):
    bs = int(dt * fs)
    bins = range(bs, len(data), bs)
    chunked = np.split(data, bins)
    for i, c in enumerate(chunked[:-1]):
        t = (i + 1.) * bs / fs
        yield t, rms(c)

def timeslice(fs, data, dt, channel=0):
    x, y = zip(*list(it_timeslice(fs, data, dt)))
    try:
        return np.array(x), np.array(y)[:,channel]
    except IndexError:
        return np.array(x), np.array(y)
        

def mol(fs, data, dt, bpf):
    t, signal = timeslice(fs, data, dt)
    _, harm3 = timeslice(fs, bpf(fs, data), dt)
    thd = 100. * harm3 / signal
    return t, db(signal), thd

def mol_1k(fs, data, dt):
    return mol(fs, data, dt, filters.thd_for_1k)

def mol_315(fs, data, dt):
    return mol(fs, data, dt, filters.thd_for_315)

def thd(fs, data, bpf):
    harm3 = rms(bpf(fs, data))
    return 100. * harm3 / rms(data)

def thd_1k(fs, data):
    return thd(fs, data, filters.thd_for_1k)

def thd_315(fs, data):
    return thd(fs, data, filters.thd_for_315)

def find_mol(lvl, thd, limit=3.):
    return lvl[thd < limit][-1]

def sol(fs, data, dt):
    t, level = timeslice(fs, data, dt)
    return t, db(level)
