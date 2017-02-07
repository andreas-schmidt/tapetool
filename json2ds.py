# coding: utf-8

from __future__ import print_function

import json
from math import log10
import numpy as np

def fit(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    cov = np.sum((x - x_mean) * (y - y_mean))
    var = np.sum((x - x_mean)**2)
    a = cov / var
    b = y_mean - a * x_mean
    return lambda x1: a * x1 + b

def fit_thd(mol_data, lvl=0.):
    x = np.array(mol_data['lvl'])
    y = np.array(mol_data['thd'])
    cut = (x > lvl-1) * (x < lvl+1)
    f = fit(x[cut], y[cut])
    return f(lvl)

def fit_mol(mol_data):
    x = np.array(mol_data['thd'])
    y = np.array(mol_data['lvl'])
    cut = (x > -32) * (x < -28)
    f = fit(x[cut], y[cut])
    return f(-30.46)

data = json.load(open("test1.json"))

out = open('datasheet.dat', 'w')
for b, m in data:
    print(
            b,
            20 * log10(b / 0.5),
            m['reflevel'],
            fit_thd(m['mol_data']),
            m['s01'],
            m['s10'],
            m['s16'],
            fit_mol(m['mol_data']),
            m['sol10'],
            m['sol16'],
            m['noise'],
            file=out)
out.close()    
