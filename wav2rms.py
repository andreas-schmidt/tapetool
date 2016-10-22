#!/usr/bin/env python

from __future__ import print_function

import sys

import numpy as np
from scipy.io import wavfile

def wav2rms(filename, outfile):
    fs, data = wavfile.read(filename)
    bs = int(0.1 * fs)
    norm = data * 1. / np.iinfo(data.dtype).max
    bins = range(bs, len(data), bs)
    chunked = np.split(norm, bins)
    for i, c in enumerate(chunked[:-1]):
        rms = np.sqrt(1. * np.sum(c**2, axis=0) / len(c))
        print(
            i,
            (i + 1.) * bs / fs,
            *db(rms),
            file=outfile)

def db(x):
    return 20 * np.log10(x)

def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        print('usage {} <filename>'.format(sys.argv[0]))
        sys.exit()

    outfilename = filename[:-3] + 'dat'

    with open(outfilename, 'w') as outfile:
        wav2rms(filename, outfile)
    
if __name__ == '__main__':
    main()
