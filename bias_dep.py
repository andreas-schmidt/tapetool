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
    i_reflevel = tth.cut(fs,  1.0, 5)
    i_thd =      tth.cut(fs,  6.5, 5)
    i_mol =      tth.cut(fs, 12.0, 5)
    i_sol10 =    tth.cut(fs, 17.5, 5)
    i_sol16 =    tth.cut(fs, 23.0, 5)

    # select the right filter for THD measurements
    filter_thd = ttf.thd_for_1k

    # reference level
    result['reflevel'] = tth.db(tth.rms(data[i_reflevel])) - cal

    # THD
    result['thd'] = tta.db(.01 * tta.thd(fs, data[i_reflevel], filter_thd))

    # MOL
    t, lvl, thd = tta.mol(fs, data[i_mol], 0.05, filter_thd)
    result['mol'] = tta.find_mol(lvl, thd) - cal
    result['mol_data'] = dict()
    result['mol_data']['t'] = list(t)
    result['mol_data']['lvl'] = list(lvl)
    result['mol_data']['thd'] = list(thd)

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
            (0.108, 'b00.wav'),
            (0.132, 'b01.wav'),
            (0.160, 'b02.wav'),
            (0.199, 'b03.wav'),
            (0.249, 'b04.wav'),
            (0.319, 'b05.wav'),
            (0.403, 'b06.wav'),
            (0.452, 'b07.wav'),
            (0.493, 'b08.wav'),
            (0.561, 'b09.wav'),
            (0.629, 'b10.wav'),
            (0.684, 'b11.wav'),
            (0.794, 'b12.wav'),
            (0.909, 'b13.wav'),
    ]:
        out.append((b, main(wavfile, cal)))
    json.dump(out, open('test.json', 'w'))

