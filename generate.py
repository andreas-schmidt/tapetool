#!/usr/bin/env python

import numpy as np
from scipy.io import wavfile
from scipy.signal import chirp

fs = 48000

def silence(fs, t):
    return np.zeros(fs * t, dtype=float)

def sin(fs, f, t):
    T = int(t * fs / f) * f
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

def lvl(db):
    return 10**(db/20.)

audio = [
    silence(fs, 10),
    lvl(-10) * sin(fs, 1000, 30),
    lvl(-30) * linsweep(fs, 20, 10, 2000),
    lvl(-10) * sin(fs, 1000, 1),
    lvl(-30) * logsweep(fs, 10, 20, 20000),
    lvl(-10) * sin(fs, 1000, 20),
    lvl(-30) * linsweep(fs, 20, 10, 1000),
    lvl(-10) * sin(fs, 1000, 1),
    lvl(-30) * logsweep(fs, 10, 20, 20000),
    lvl(-10) * sin(fs, 1000, 20),
    lvl(-30) * linsweep(fs, 20, 10, 500),
    lvl(-10) * sin(fs, 1000, 1),
    lvl(-30) * logsweep(fs, 10, 20, 20000),
    lvl(-10) * sin(fs, 1000, 20),
    silence(fs, 10),
]

wavfile.write('chirp.wav', fs,
              np.array(np.concatenate(audio) * np.iinfo(np.int32).max,
              dtype=np.int32))

