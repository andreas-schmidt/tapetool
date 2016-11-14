import numpy as np

from generate import silence, sin, logsweep, linramp, dbramp
from helpers import lvl, write_wav

fs = 96000

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

write_wav(fs, np.concatenate(audio), 'testsignal.wav')

