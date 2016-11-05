#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/lib
export PATH=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/build/lib:$PATH
export LD_LIBRARY_PATH=/home/agrim/Desktop/FHSS_Pro/gr-FHSS/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-FHSS 
