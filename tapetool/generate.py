import numpy as np
from scipy.io import wavfile
from scipy.signal import chirp

from tapetool.helpers import lvl

def silence(fs, t):
    return np.zeros(int(fs * t), dtype=float)

def sin(fs, t, f):
    T = int(t * fs)
    return np.sin(np.arange(T) * 2*np.pi * f/fs)

def sweep(fs, t, f1, f2, method):
    return chirp(np.arange(fs*t),
                 1.*f1/fs,
                 fs*t,
                 1.*f2/fs,
                 method=method,
                 phi=270)

def linsweep(fs, t, f1, f2):
    return sweep(fs, t, f1, f2, 'linear')

def logsweep(fs, t, f1, f2):
    return sweep(fs, t, f1, f2, 'logarithmic')

def dbramp(fs, t, l1, l2):
    T = int(t * fs)
    slope = float(l2 - l1) / T
    return lvl(l1 + slope * np.arange(T))

def linramp(fs, t, l1, l2):
    T = int(t * fs)
    a1, a2 = lvl(l1), lvl(l2)
    slope = float(a2 - a1) / T
    return a1 + slope * np.arange(T)

