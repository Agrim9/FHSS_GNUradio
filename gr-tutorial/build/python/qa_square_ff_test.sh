#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/harshvardhan/Desktop/commLab/gr-tutorial/python
export PATH=/home/harshvardhan/Desktop/commLab/gr-tutorial/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/harshvardhan/Desktop/commLab/gr-tutorial/build/swig:$PYTHONPATH
/usr/bin/python2 /home/harshvardhan/Desktop/commLab/gr-tutorial/python/qa_square_ff.py 
