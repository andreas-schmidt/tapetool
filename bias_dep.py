from __future__ import print_function
from __future__ import division

import numpy as np

import tapetool.helpers as tth
import tapetool.analysis as tta
import tapetool.filters as ttf

def main(wavfile, cal):
    result = dict()
    result['cal'] = cal
    result['source'] = dict()
    result['source']['filename'] = wavfile

    fs, data = tth.read_wav(wavfile)
    result['source']['fs'] = fs
    result['source']['samples'] = len(data)
    result['source']['seconds'] = len(data) / fs

    # where to find what parts of audio in the test file
    i_reflevel = tth.cut(fs,  0.5,  1.)
    i_noise    = tth.cut(fs,  2.0,  3.)
    i_s01      = tth.cut(fs,  5.5,  1.)
    i_s10      = tth.cut(fs,  6.5,  1.)
    i_s16      = tth.cut(fs,  7.5,  1.)
    i_mol      = tth.cut(fs,  9.0, 10.)
    i_sol10    = tth.cut(fs, 19.5,  5.)
    i_sol16    = tth.cut(fs, 25.0,  5.)

    # select the right filter for THD measurements
    filter_thd = ttf.thd_for_1k

    # reference level
    result['reflevel'] = tth.db(tth.rms(data[i_reflevel])) - cal
    result['thd'] = tta.db(.01 * tta.thd(fs, data[i_reflevel], filter_thd))

    # noise
    result['noise'] = tth.db(tth.rms(data[i_noise])) - cal

    # sensitivity
    result['s01'] = tth.db(tth.rms(data[i_s01])) - cal
    result['s10'] = tth.db(tth.rms(data[i_s10])) - cal
    result['s16'] = tth.db(tth.rms(data[i_s16])) - cal

    # THD
    result['thd'] = tta.db(.01 * tta.thd(fs, data[i_reflevel], filter_thd))

    # MOL
    t, lvl, thd = tta.mol(fs, data[i_mol], 0.05, filter_thd)
    result['mol'] = tta.find_mol(lvl, thd) - cal
    result['mol_data'] = dict()
    result['mol_data']['t'] = list(t)
    result['mol_data']['lvl'] = list(lvl - cal)
    result['mol_data']['thd'] = list(tta.db(.01 * thd))

    # SOL10
    x, y = tta.sol(fs, data[i_sol10], 0.1)
    i = np.argmax(y)
    result['sol10'] = y[i] - cal
    result['sol10_data'] = dict()
    result['sol10_data']['at'] = x[i]
    result['sol10_data']['t'] = list(x)
    result['sol10_data']['lvl'] = list(y)
    
    # SOL16
    x, y = tta.sol(fs, data[i_sol16], 0.1)
    i = np.argmax(y)
    result['sol16'] = y[i] - cal
    result['sol16_data'] = dict()
    result['sol16_data']['at'] = x[i]
    result['sol16_data']['t'] = list(x)
    result['sol16_data']['lvl'] = list(y)
    
    return result

if __name__ == '__main__':
    import json
    out = list()
    cal = -20.55
    for b, wavfile in [
            (0.134, '03-b01.wav'),
            (0.156, '04-b02.wav'),
            (0.197, '05-b03.wav'),
            (0.251, '06-b04.wav'),
            (0.315, '07-b05.wav'),
            (0.397, '08-b06.wav'),
            (0.448, '09-b07.wav'),
            (0.502, '10-b08.wav'),
            (0.559, '11-b09.wav'),
            (0.618, '12-b10.wav'),
            (0.667, '13-b11.wav'),
            (0.715, '14-b12.wav'),
            (0.835, '15-b13.wav'),
            (0.975, '16-b14.wav'),
    ]:
        out.append((b, main(wavfile, cal)))
    json.dump(out, open('test1.json', 'w'))

