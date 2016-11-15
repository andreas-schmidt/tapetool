#!/usr/bin/env python

from __future__ import print_function

import sys

from tapetool.helpers import read_wav, db
from tapetool.analysis import timeslice

try:
    filename = sys.argv[1]
except IndexError:
    print('usage {} <filename>'.format(sys.argv[0]))
    sys.exit()

fs, data = read_wav(filename)
channels = data.shape[1]

columns = list()
for c in range(channels):
    t, r = timeslice(fs, data, 0.1, c)
    if not columns:
        columns.append(t)
    columns.append(db(r))

outfilename = filename[:-3] + 'dat'
with open(outfilename, 'w') as out:
    for row in zip(*columns):
        print(*row, file=out)

