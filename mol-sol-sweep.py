from __future__ import print_function

import numpy as np

import tapetool.helpers as tth
import tapetool.analysis as tta
import tapetool.filters as ttf

def main(wavfile, prefix, offset=0.):
    print('prefix is "{}"'.format(prefix))
    print('using wave file "{}" as input'.format(wavfile))
    fs, data = tth.read_wav(wavfile)
    print('sample rate is {} Hz, read {} samples ({} seconds)'.format(
        fs,
        len(data),
        1. * len(data) / fs))
    
    # where to find what parts of audio in the test file
    i_ref_315 = tth.cut(fs,  0.5 + offset, 1)
    i_ref_1k  = tth.cut(fs,  2.5 + offset, 1)
    i_noise   = tth.cut(fs,  4.5 + offset, 4)
    i_mol_315 = tth.cut(fs,  9.5 + offset, 5)
    i_mol_1k  = tth.cut(fs, 15.5 + offset, 5)
    i_sol_6k3 = tth.cut(fs, 21.5 + offset, 5)
    i_sol_10k = tth.cut(fs, 27.5 + offset, 5)
    i_sol_16k = tth.cut(fs, 33.5 + offset, 5)
    i_sweep   = tth.cut(fs, 39.5 + offset, 20)

    print('ref 315    :', tth.db(tth.rms(data[i_ref_315])))
    print('THD ref 315:', tta.thd(fs, data[i_ref_315], ttf.thd_for_315))
    print('ref 1k     :', tth.db(tth.rms(data[i_ref_1k])))
    print('THD ref 1k :', tta.thd(fs, data[i_ref_1k], ttf.thd_for_1k))
    print('noise (unw):', tth.db(tth.rms(data[i_noise])))

    mol(fs, data, prefix, i_mol_315, '315', ttf.thd_for_315)
    mol(fs, data, prefix, i_mol_1k, '1k', ttf.thd_for_1k)

    sol(fs, data, prefix, i_sol_6k3, '6k3')
    sol(fs, data, prefix, i_sol_10k, '10k')
    sol(fs, data, prefix, i_sol_16k, '16k')

    # sweep 15 Hz to 24 kHz
    t, l = tta.timeslice(fs, data[i_sweep], 0.05, 0)
    t, r = tta.timeslice(fs, data[i_sweep], 0.05, 1)
    f = [15 * (24000./15)**(i/20.) for i in t]
    np.savetxt('{}-sweep.dat'.format(prefix),
               np.transpose([t, f, tth.db(l), tth.db(r)]),
               fmt='%-10.6g')

def mol(fs, data, prefix, i_mol, name, flt):
    t, lvl, thd = tta.mol(fs, data[i_mol], 0.05, flt)
    np.savetxt('{}-mol-{}.dat'.format(prefix, name),
               np.transpose([t, lvl, thd]),
               fmt='%-10.6g')
    print("MOL {:8}: {:6.2f}dB".format(
        '3%',
        tta.find_mol(lvl, thd)
        ))

def sol(fs, data, prefix, i_sol, name):
    x, y = tta.sol(fs, data[i_sol], 0.1)
    i = np.argmax(y)
    np.savetxt('{}-sol-{}.dat'.format(prefix, name),
               np.transpose([x, y]),
               fmt='%-10.6g')
    print('SOL {:8}: {:6.2f}dB at {}s'.format(
        name,
        y[i],
        x[i]
        ))

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('wavfile', help='wave file with test signal')
    ap.add_argument('prefix', help='prefix to use for output files')
    ap.add_argument('--offset', type=float, default=0.,
                    help='shift from reference in s')
    args = ap.parse_args()

    main(args.wavfile, args.prefix, offset=args.offset)

