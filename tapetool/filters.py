from scipy.signal import butter, lfilter

def butter_bandpass(fs, data, f1=2900, f2=3100):
    w1 = f1 / 0.5 / fs
    w2 = f2 / 0.5 / fs
    b, a = butter(N=3, Wn=[w1, w2], btype='band')
    return lfilter(b, a, data, axis=0)

def thd_for_1k(fs, data):
    return butter_bandpass(fs, data, 2900, 3100)

def thd_for_315(fs, data):
    return butter_bandpass(fs, data, 910, 980)

