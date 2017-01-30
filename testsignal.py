import numpy as np

from tapetool.generate import silence, sin, logsweep, linsweep, linramp, dbramp
from tapetool.helpers import lvl, write_wav

cl19 = [0.03,  0.  , -0.62, -1.53, -2.38, -3.  , -3.93]
cr19 = [0.03, -0.  , -0.65, -1.58, -2.45, -3.07, -3.99]
cl38 = [0.02,  0.  , -0.47, -1.17, -1.83, -2.31, -3.06]
cr38 = [0.03, -0.  , -0.55, -1.26, -1.93, -2.41, -3.16]
fcorr = cl38 #[0 for i in range(7)]

def generate_signal(fs, f_ref):
    return [
        silence(fs, 1),
        lvl(-10 + fcorr[0]) * sin(fs, 10, 315), silence(fs, 0.5),
        lvl(-10 + fcorr[1]) * sin(fs, 10, 1000), silence(fs, 0.5),
        lvl(-10 + fcorr[2]) * sin(fs, 10, 6300), silence(fs, 0.5),
        lvl(-10 + fcorr[3]) * sin(fs, 10, 10000), silence(fs, 0.5),
        lvl(-10 + fcorr[4]) * sin(fs, 10, 12500), silence(fs, 0.5),
        lvl(-10 + fcorr[5]) * sin(fs, 10, 14000), silence(fs, 0.5),
        lvl(-10 + fcorr[6]) * sin(fs, 10, 16000), silence(fs, 0.5),
#       lvl(-40) * logsweep(fs, 10, 20, 20000), silence(fs, 0.5),
#       lvl(-40) * logsweep(fs, 20, 10, 40000), silence(fs, 0.5),
#       lvl(-40) * linsweep(fs, 10, 10, 1000), silence(fs, 0.5),
#       linramp(fs, 5, -30, 0) * sin(fs, 5, 1000), silence(fs, 0.5),
#       dbramp(fs, 5, -30, 0) * sin(fs, 5,  6300), silence(fs, 0.5),
#       dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000), silence(fs, 0.5),
#       dbramp(fs, 5, -30, 0) * sin(fs, 5, 12500), silence(fs, 0.5),
#       dbramp(fs, 5, -30, 0) * sin(fs, 5, 14000), silence(fs, 0.5),
#       dbramp(fs, 5, -30, 0) * sin(fs, 5, 16000), silence(fs, 0.5),
        silence(fs, 0.5),
    ]

def gen_b77hs_19l(fs):
    return [
        silence(fs, 0.5),
        lvl(-20) * sin(fs, 1, 1000), silence(fs, 0.5),
        silence(fs, 3.5),
#       lvl(-40 + cl19[0]) * sin(fs, 1, 315),
        lvl(-40 + cl19[1]) * sin(fs, 1, 1000),
#       lvl(-40 + cl19[2]) * sin(fs, 1, 6300),
        lvl(-40 + cl19[3]) * sin(fs, 1, 10000),
#       lvl(-40 + cl19[4]) * sin(fs, 1, 12500),
#       lvl(-40 + cl19[5]) * sin(fs, 1, 14000),
        lvl(-40 + cl19[6]) * sin(fs, 1, 16000), silence(fs, 0.5),
        linramp(fs, 5, -25, -15) * sin(fs, 5, 1000), silence(fs, 0.5),
        dbramp(fs, 5, -25, -15) * sin(fs, 5, 1000), silence(fs, 0.5),
        linramp(fs, 5, -30, 0) * sin(fs, 5, 1000), silence(fs, 0.5),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 10000), silence(fs, 0.5),
#       dbramp(fs, 5, -30, 0) * sin(fs, 5, 12500), silence(fs, 0.5),
        dbramp(fs, 5, -30, 0) * sin(fs, 5, 16000), silence(fs, 0.5),
        silence(fs, 0.5),
    ]

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--rate', type=int, default=96000,
                    help='sampling rate in Hz, default is 96000')
    ap.add_argument('--slow', action='store_true',
                    help='use 315Hz as reference frequency')
    args = ap.parse_args()

    fs = args.rate
    f_ref = 315 if args.slow else 1000

    audio = gen_b77hs_19l(fs)
    write_wav(fs, np.concatenate(audio), 'b77hs_19l.wav')

