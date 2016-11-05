#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/python
export PATH=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/build/python:$PATH
export LD_LIBRARY_PATH=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/build/swig:$PYTHONPATH
/usr/bin/python2 /home/agrim/Desktop/FHSS_Pro/gr-FHSS/python/qa_freq_selector.py 
