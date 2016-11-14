# coding: utf-8

from helpers import read_wav, db, rms
import filters

def main(filename):
    fs, data = read_wav(filename)
    db_sig, db_h3, k3 = calc_k3(fs, data)
    print '{:22}: total {:2.1f}dB, h3 {:2.1f}dB, k3 {:5.2f}%'.format(
        filename, db_sig, db_h3, k3
    )

def calc_k3(fs, data):
    h3 = filters.thd_for_1k(fs, data)
    return db(rms(data)), db(rms(h3)), 100. * rms(h3) / rms(data)

if __name__ == '__main__':
    main('1k+3k75+25Summe.wav')
    main('1k+3klr97+3summe.wav')
    main('1k+3klr3ProzSumme.wav')

