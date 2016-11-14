# coding: utf-8

import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, lfilter

def main(filename):
    fs, data = read_wav(filename)
    db_sig, db_h3, k3 = calc_k3(fs, data)
    print '{:22}: total {:2.1f}dB, h3 {:2.1f}dB, k3 {:5.2f}%'.format(
        filename, db_sig, db_h3, k3
    )

def read_wav(filename):
    fs, samples = wavfile.read(filename)
    return fs, samples2float(samples)

def samples2float(data):
    # divide by the largest number for this data type
    return 1. * data / np.iinfo(data.dtype).max

def calc_k3(fs, data):
    h3 = filter_h3(fs, data)
    return db(rms(data)), db(rms(h3)), 100. * rms(h3) / rms(data)

def filter_h3(fs, data, f1=2900, f2=3100):
    w1 = f1 / 0.5 / fs
    w2 = f2 / 0.5 / fs
    b, a = butter(N=3, Wn=[w1, w2], btype='band')
    return lfilter(b, a, data, axis=0)

def db(x):
    return 20 * np.log10(x)

def rms(x):
    return np.sqrt(np.sum(x**2, axis=0) / len(x))

if __name__ == '__main__':
    main('1k+3k75+25Summe.wav')
    main('1k+3klr97+3summe.wav')
    main('1k+3klr3ProzSumme.wav')

