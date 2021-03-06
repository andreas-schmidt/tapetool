import numpy as np

from tapetool.generate import silence, sin, logsweep, linsweep, linramp, dbramp
from tapetool.helpers import lvl, write_wav

cl19 = [0.03,  0.  , -0.62, -1.53, -2.38, -3.  , -3.93]
cr19 = [0.03, -0.  , -0.65, -1.58, -2.45, -3.07, -3.99]
cl38 = [0.02,  0.  , -0.47, -1.17, -1.83, -2.31, -3.06]
cr38 = [0.03, -0.  , -0.55, -1.26, -1.93, -2.41, -3.16]
#fcorr = cl38
fcorr = [0., 0., 0., 0., 0., 0., 0.]

def generate_signal(fs, f_ref):
    return [
        silence(fs, 0.5),
        lvl(-10 + fcorr[0]) * sin(fs, 10, 315), silence(fs, 0.5),
        lvl(-10 + fcorr[1]) * sin(fs, 10, 1000), silence(fs, 0.5),
        lvl(-10 + fcorr[2]) * sin(fs, 10, 6300), silence(fs, 0.5),
        lvl(-10 + fcorr[3]) * sin(fs, 10, 10000), silence(fs, 0.5),
        lvl(-10 + fcorr[4]) * sin(fs, 10, 12500), silence(fs, 0.5),
        lvl(-10 + fcorr[5]) * sin(fs, 10, 14000), silence(fs, 0.5),
        lvl(-10 + fcorr[6]) * sin(fs, 10, 16000), silence(fs, 0.5),
        silence(fs, 0.5),
    ]

def gen_b77hs_19l(fs):
    return np.concatenate([
        silence(fs, 0.5),
        lvl(-20) * sin(fs, 1, 1000), silence(fs, 0.5),
        silence(fs, 3.5),
#       lvl(-40 + cl19[0]) * sin(fs, 1, 315),
        lvl(-40 + cl19[1]) * sin(fs, 1, 1000),
        lvl(-40 + cl19[2]) * sin(fs, 1, 6300),
        lvl(-40 + cl19[3]) * sin(fs, 1, 10000),
#       lvl(-40 + cl19[4]) * sin(fs, 1, 12500),
#       lvl(-40 + cl19[5]) * sin(fs, 1, 14000),
        lvl(-40 + cl19[6]) * sin(fs, 1, 16000), silence(fs, 0.5),
        dbramp(fs, 10, -30, 0) * sin(fs, 10, 1000), silence(fs, 0.5),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000), silence(fs, 0.5),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 16000), silence(fs, 0.5),
        silence(fs, 0.5),
    ])

def gen_b77hs_38l(fs):
    return np.concatenate([
        silence(fs, 0.5),
        lvl(-20) * sin(fs, 1, 1000), silence(fs, 0.5),
        silence(fs, 3.5),
#       lvl(-40 + cl38[0]) * sin(fs, 1, 315),
        lvl(-40 + cl38[1]) * sin(fs, 1, 1000),
#       lvl(-40 + cl38[2]) * sin(fs, 1, 6300),
        lvl(-40 + cl38[3]) * sin(fs, 1, 10000),
#       lvl(-40 + cl38[4]) * sin(fs, 1, 12500),
#       lvl(-40 + cl38[5]) * sin(fs, 1, 14000),
        lvl(-40 + cl38[6]) * sin(fs, 1, 16000), silence(fs, 0.5),
        dbramp(fs, 10, -30, 0) * sin(fs, 10, 1000), silence(fs, 0.5),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000), silence(fs, 0.5),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 16000), silence(fs, 0.5),
        silence(fs, 0.5),
    ])

def gen_sweep(fs):
    return np.concatenate([
        silence(fs, 0.5),
        lvl(-20) * sin(fs, 1, 1000), silence(fs, 0.5),
        lvl(-40) * logsweep(fs, 10, 20, 20000), silence(fs, 0.5),
        lvl(-40) * linsweep(fs, 10, 20, 20000), silence(fs, 0.5),
    ])

def gen_test(fs):
    return np.concatenate([
        silence(fs, 0.5),
        lvl(-20) * sin(fs, 1,  315), silence(fs, 1.0),
        lvl(-20) * sin(fs, 1, 1000), silence(fs, 1.0),
        silence(fs, 5.0),
        dbramp(fs, 5, -30, 0) * sin(fs, 5,   315), silence(fs, 1.),
        dbramp(fs, 5, -30, 0) * sin(fs, 5,  1000), silence(fs, 1.),
        dbramp(fs, 5, -30, 0) * sin(fs, 5,  6300), silence(fs, 1.),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000), silence(fs, 1.),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 16000), silence(fs, 1.),
        lvl(-40) * logsweep(fs, 20, 15, 24000), silence(fs, 1.),
    ])


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--rate', type=int, default=96000,
                    help='sampling rate in Hz, default is 96000')
    args = ap.parse_args()
    fs = args.rate

    write_wav(fs, gen_test(fs), 'mol-sol-sweep.wav')
    write_wav(fs, lvl(-20) * sin(fs, 60, 1000), 'sin-1000.wav')
    write_wav(fs, lvl(-20) * sin(fs, 60, 315), 'sin-315.wav')

#   write_wav(fs, gen_b77hs_19l(fs), 'b77hs_19l.wav')
#   write_wav(fs, gen_b77hs_38l(fs), 'b77hs_38l.wav')
#   write_wav(fs, gen_sweep(fs), 'sweep.wav')
