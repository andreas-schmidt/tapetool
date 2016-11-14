#!/usr/bin/env python

import numpy as np
from scipy.io import wavfile
from scipy.signal import chirp

fs = 96000

def silence(fs, t):
    return np.zeros(fs * t, dtype=float)

def sin(fs, f, t):
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

def lvl(db):
    return 10**(db/20.)

audio = [
    silence(fs, 5),
    lvl(-10) * sin(fs, 315, 10),
    silence(fs, 1),
    lvl(-10) * sin(fs, 1000, 10),
    silence(fs, 1),
    lvl(-30) * logsweep(fs, 20, 10, 40000),
    silence(fs, 1),
    linramp(fs, 10, -30, 0) * sin(fs,   315, 10),
    linramp(fs, 10, -30, 0) * sin(fs,  1000, 10),
    dbramp(fs, 5, -30, 0) * sin(fs,   315, 5),
    dbramp(fs, 5, -30, 0) * sin(fs,  1000, 5),
    dbramp(fs, 5, -30, 0) * sin(fs,  6300, 5),
    dbramp(fs, 5, -30, 0) * sin(fs, 10000, 5),
    dbramp(fs, 5, -30, 0) * sin(fs, 12500, 5),
    dbramp(fs, 5, -30, 0) * sin(fs, 14000, 5),
    dbramp(fs, 5, -30, 0) * sin(fs, 16000, 5),
    silence(fs, 5),
]

wavfile.write('testsignal.wav', fs,
              np.array(np.concatenate(audio) * np.iinfo(np.int32).max,
              dtype=np.int32))

