Tapetool
========

A collection of tools for measuring the recording performance of magnetic audio tape with your sound card:

1. generate a test signal in a wave-file with `generate.py`
2. record it onto the tape under test and digitise the played back signal using your favourite audio editor
3. analyse properties like MOL, SOL and THD using the tools from this package

Installation
------------

Unfortunately, there is no install or `setup.py` yet. Currently, you have to clone the source code into a local folder and run it directly there. The requirements for running it are:

* Python 2 (tested with Python 2.7.2 on Ubuntu 12.04 and Python 2.7.12 on Ubuntu 16.04)
* NumPy
* SciPy, in particular `scipy.io` and `scipy.signal`
* [Gnuplot](http://gnuplot.info/) if you want to use the plotting examples

Licensing
---------

The code in this project is licensed under MIT license.

