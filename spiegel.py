#!/usr/bin/env python

from __future__ import print_function

import numpy as np
from scipy.io import wavfile

def lmbinv(i, speed, fs, f1):
    f0 = 10.
    t1 = 20.
    freq = f0 + (f1 - f0) * i / fs / t1
    return freq / speed

def db(x):
    return 20 * np.log10(x)

def run(fs, data, speed, length, outfile, f1, ref):
    bs = int(fs * length)
    norm = data * 1. / np.iinfo(data.dtype).max
    bins = range(bs, len(data), bs)
    chunked = np.split(norm, bins)
    for i, c in enumerate(chunked[:-1]):
        rms = np.sqrt(1. * np.sum(c**2, axis=0) / len(c))
        print(
            i,
            lmbinv(bins[i], speed, fs, f1),
            *db(rms / ref),
            file=outfile)

def tts(fs, t0, t1):
    return slice(int(t0 * fs + 1), int(t1 * fs))
    
def get_reflevel(fs, data, s1):
    c = 1. * data[tts(fs, s1 - 1., s1)] / np.iinfo(data.dtype).max
    return np.sqrt(1. * np.sum(c**2, axis=0) / len(c))

def main(prefix, s1, s2, s3, title):
    fs, data = wavfile.read(prefix + '.wav')
    length = .1

    ref = get_reflevel(fs, data, s1)
    print(prefix, ref)

    def r(t0, f1, speed, out):
        run(fs,
            data[tts(fs, t0, t0 + 20.)],
            speed,
            length,
            open(out, 'w'),
            f1,
            ref)

    r(s1, 2000., .1905, prefix + '-1905.dat')
    r(s2, 1000., .0953, prefix + '-0953.dat')
    r(s3,  500., .0476, prefix + '-0476.dat')

    template = open('template.plt').read()
    plt_l = template.format(title='L ' + title, prefix=prefix, col=3)
    plt_r = template.format(title='R ' + title, prefix=prefix, col=4)
    open(prefix + '-l.plt', 'w').write(plt_l)
    open(prefix + '-r.plt', 'w').write(plt_r)

if __name__ == '__main__':
    main('k-4502', 40.222818, 91.359767, 142.636910, '4502 Halbspur Woelke')
    main('k-5002', 40.224331, 91.363238, 142.645018, '5002 Halbspur Woelke')
    main('k-6002', 25.648929, 76.788175, 128.070287, '6002 Halbspur Bogen (?)')
    main('k-6004', 19.291440, 70.427377, 121.702700, '6004 Viertelspur Ferrotronic')
    main('k-vorb', 40.085222, 91.085239, 142.085246, 'vorband')
