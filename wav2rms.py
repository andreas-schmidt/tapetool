#!/usr/bin/env python

from __future__ import print_function

import sys

from tapetool.helpers import read_wav, db
from tapetool.analysis import it_timeslice

try:
    filename = sys.argv[1]
except IndexError:
    print('usage {} <filename>'.format(sys.argv[0]))
    sys.exit()

outfilename = filename[:-3] + 'dat'

with open(outfilename, 'w') as outfile:
    fs, data = read_wav(filename)
    for t, r in it_timeslice(fs, data, 0.1):
        try:
            print(t, *db(r), file=outfile)
        except TypeError:
            # if r is not iterable, it's only one channel
            print(t, db(r), file=outfile)

