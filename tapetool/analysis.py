import numpy as np
from helpers import rms, db
import filters

def it_timeslice(fs, data, dt):
    bs = int(dt * fs)
    bins = range(bs, len(data), bs)
    chunked = np.split(data, bins)
    for i, c in enumerate(chunked[:-1]):
        t = (i + 1.) * bs / fs
        yield t, rms(c)

def timeslice(fs, data, dt, channel=0):
    x, y = zip(*list(it_timeslice(fs, data, dt)))
    return np.array(x), np.array(y)[:,channel]

def mol(fs, data, dt, bpf):
    t, signal = timeslice(fs, data, dt)
    _, harm3 = timeslice(fs, bpf(fs, data), dt)
    thd = 100. * harm3 / signal
    return t, db(signal), thd

def mol_1k(fs, data, dt):
    return mol(fs, data, dt, filters.thd_for_1k)

def mol_315(fs, data, dt):
    return mol(fs, data, dt, filters.thd_for_315)

