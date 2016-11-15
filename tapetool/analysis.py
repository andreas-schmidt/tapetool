import numpy as np
from helpers import rms

def it_timeslice(fs, data, dt=0.1):
    bs = int(dt * fs)
    bins = range(bs, len(data), bs)
    chunked = np.split(data, bins)
    for i, c in enumerate(chunked[:-1]):
        t = (i + 1.) * bs / fs
        yield i, t, rms(c)

