from tapetool.helpers import read_wav, db, rms
import tapetool.filters

for filename in (
        '1k+3k75+25Summe.wav',
        '1k+3klr97+3summe.wav',
        '1k+3klr3ProzSumme.wav'):
    fs, data = read_wav(filename)
    h3 = tapetool.filters.thd_for_1k(fs, data)
    print '{:22}: total {:2.1f}dB, h3 {:2.1f}dB, k3 {:5.2f}%'.format(
        filename,
        db(rms(data)),
        db(rms(h3)),
        100. * rms(h3) / rms(data)
    )
