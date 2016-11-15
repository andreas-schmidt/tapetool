import numpy as np
from helpers import rms

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
