#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/agrim/Desktop/EE_340_Submission/gr-mod_64/python
export PATH=/home/agrim/Desktop/EE_340_Submission/gr-mod_64/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/agrim/Desktop/EE_340_Submission/gr-mod_64/build/swig:$PYTHONPATH
/usr/bin/python2 /home/agrim/Desktop/EE_340_Submission/gr-mod_64/python/qa_freq_selector.py 
