#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/agrim/Desktop/340_PROJECT/gr-FHSS/python
export PATH=/home/agrim/Desktop/340_PROJECT/gr-FHSS/lib/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/agrim/Desktop/340_PROJECT/gr-FHSS/lib/swig:$PYTHONPATH
/usr/bin/python2 /home/agrim/Desktop/340_PROJECT/gr-FHSS/python/qa_square_ff.py 
