import numpy as np

from tapetool.generate import silence, sin, logsweep, linramp, dbramp
from tapetool.helpers import lvl, write_wav

fs = 96000

audio = [
    silence(fs, 1),
    lvl(-10) * sin(fs, 5, 315),
    silence(fs, 0.5),
    linramp(fs, 5, -30, 0) * sin(fs, 5,   315),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5,  6300),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 12500),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 14000),
    silence(fs, 1),
]

write_wav(fs, np.concatenate(audio), 'testsignal-slow.wav')

audio = [
    silence(fs, 1),
    lvl(-10) * sin(fs, 5, 1000),
    silence(fs, 0.5),
    linramp(fs, 5, -30, 0) * sin(fs, 5,  1000),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5,  6300),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 12500),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 14000),
    silence(fs, 0.5),
    dbramp(fs, 5, -30, 0) * sin(fs, 5, 16000),
    silence(fs, 1),
]

write_wav(fs, np.concatenate(audio), 'testsignal-fast.wav')

