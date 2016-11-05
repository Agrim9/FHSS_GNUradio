#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/harshvardhan/Desktop/commLab/gr-tutorial/lib
export PATH=/home/harshvardhan/Desktop/commLab/gr-tutorial/build/lib:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-tutorial 
