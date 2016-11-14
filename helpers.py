import numpy as np
from scipy.io import wavfile

def read_wav(filename):
    fs, samples = wavfile.read(filename)
    return fs, samples2float(samples)

def samples2float(data):
    # divide by the largest number for this data type
    return 1. * data / np.iinfo(data.dtype).max

def db(x):
    return 20 * np.log10(x)

def rms(x):
    return np.sqrt(np.sum(x**2, axis=0) / len(x))


