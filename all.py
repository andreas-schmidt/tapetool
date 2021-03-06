from __future__ import print_function

import numpy as np

import tapetool.helpers as tth
import tapetool.analysis as tta
import tapetool.filters as ttf

def main(wavfile, prefix, slow=False):
    print('prefix is "{}"'.format(prefix))
    print('using {} as reference frequency'.format(
        '315 Hz' if slow else '1 kHz'))

    print('using wave file "{}" as input'.format(wavfile))
    fs, data = tth.read_wav(wavfile)
    print('sample rate is {} Hz, read {} samples ({} seconds)'.format(
        fs,
        len(data),
        1. * len(data) / fs))
    
    # where to find what parts of audio in the test file
    i_reflevel = tth.cut(fs, 1, 5)
    i_mol = tth.cut(fs, 6.5, 5)
    sol_start = [
        (12.0, '6.3 kHz'),
        (17.5, '10 kHz'),
        (23.0, '12.5 kHz'),
        (28.5, '14 kHz'),
        (34.0, '16 kHz'),
    ]

    # select the right filter for THD measurements
    if slow:
        filter_thd = ttf.thd_for_315
    else:
        filter_thd = ttf.thd_for_1k

    # reference level
    print('reference level:', tth.db(tth.rms(data[i_reflevel])))
    print('THD at reference level:', tta.thd(fs, data[i_reflevel], filter_thd))

    # MOL
    t, lvl, thd = tta.mol(fs, data[i_mol], 0.05, filter_thd)
    np.savetxt('%s-mol.dat' % prefix,
               np.transpose([t, lvl, thd]),
               fmt='%-10.6g')
    print("MOL {:8}: {:6.2f}dB".format(
        '3%',
        tta.find_mol(lvl, thd)
        ))

    # SOL
    columns = list()
    for t0, sol_label in sol_start:
        x, y = tta.sol(fs, data[tth.cut(fs, t0, 5)], 0.1)
        i = np.argmax(y)
        print('SOL {:8}: {:6.2f}dB at {}s'.format(
            sol_label,
            y[i],
            x[i]
            ))
        if not columns:
            columns.append(x)
        columns.append(y)
    np.savetxt('%s-sol.dat' % prefix,
               np.transpose([columns]),
               fmt='%-10.6g')

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('wavfile', help='wave file with test signal')
    ap.add_argument('prefix', help='prefix to use for output files')
    ap.add_argument('--slow', action='store_true',
                    help='use 315Hz as reference frequency')
    args = ap.parse_args()

    main(args.wavfile, args.prefix, args.slow)

