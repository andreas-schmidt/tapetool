import numpy as np

from tapetool.generate import silence, sin, logsweep, linramp, dbramp
from tapetool.helpers import lvl, write_wav

def generate_signal(fs, f_ref):
    return [
        silence(fs, 1),
        lvl(-10) * sin(fs, 5, f_ref),
        silence(fs, 0.5),
        linramp(fs, 5, -30, 0) * sin(fs, 5, f_ref),
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

    audio = generate_signal(fs, f_ref)
    write_wav(fs, np.concatenate(audio), 'testsignal.wav')

