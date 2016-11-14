import numpy as np
from scipy.io import wavfile

def read_wav(filename):
    fs, samples = wavfile.read(filename)
    return fs, samples2float(samples)

def samples2float(data):
    # divide by the largest number for this data type
    return 1. * data / np.iinfo(data.dtype).max

def write_wav(fs, data, filename):
    wavfile.write(filename, fs, samples2int(data))

def samples2int(data):
    return np.array(data * np.iinfo(np.int32).max, dtype=np.int32)

def db(x):
    return 20 * np.log10(x)

def lvl(db):
    return 10**(db/20.)

def rms(x):
    return np.sqrt(np.sum(x**2, axis=0) / len(x))


