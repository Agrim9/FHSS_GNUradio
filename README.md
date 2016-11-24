# FHSS_GNUradio
Frequency Hopping Spread Spectrum (FHSS) is a method of transmitting radio signals by continuously switching ("hopping") over various frequencies dtermined by a pseudo random code. 
To know more about it, you can refer to the ppt in the repository (FHSS_intro.ppt)

We've built blocks to send PM modulated waves over 8 and 64 different frequencies, according to a maximally generated pseduo random code.

## Pre-Requisite Libraries for GNUradio :-

  1. sudo apt-get install liblog4cpp5-dev
  2. sudo apt-get install swig
  3. sudo apt-get install doxygen
  4. sudo apt-get install libcppunit-dev
  5. sudo apt-get install cppunit
  6. sudo apt-get install cppunit-dev
  7. sudo apt-get install gnuradio-dev
  8. sudo apt-get install pyhton-sphinx

## Running the code on your PC's GNUradio:-

-> To install and use the blocks in GNUradio, clone the repository, make build folder in each block's directory, copy the compile.sh in the created build folder, and run compile.sh from the build folder of each block. 
-> If you've installed GNUradio directly from the git repository, this should suffice, but if not, you will have to do a little more to get the blocks on GNUradio. Please follow Troubleshooting steps mentioned at end. By the end of troubleshooting, you should get 4 blocks : "FHSS_mod_64/8 and FHSS_demod_64/8" in your PC's GNUradio.

## Block Desciption :-
1.FHSS_demod_64 : Block for FHSS and PM demodulation for 64 frequencies version 
  - Parameters: Sampling Rate 
  - O/P : Final message signal 
  - I/P : Modulated 64 frequency hopped PM wave
2.FHSS_mod_64   : Block for FHSS and PM modulation for 64 frequencies version 
  - Parameters: Sampling Rate, Modulation Sensitivity of PM ( kp*m(t))
  - O/P : Modulated PM wave hopped over 64 frequencies
  - I/P : Message Signal
3.FHSS_demod_8  : Block for FHSS and PM demodulation for 8 frequencies version 
  - Parameters: Sampling Rate 
  - O/P : Final message signal 
  - I/P : Modulated 8 frequency hopped PM wave
4.FHSS_mod_8    : Block for FHSS and PM demodulation for 8 frequencies version 
  - Parameters: Sampling Rate, Modulation Sensitivity of PM ( kp*m(t))
  - O/P : Modulated PM wave hopped over 8 frequencies
  - I/P : Message Signal
 
## GRC Files :-
You can directly run the GRC files in the repository, for some reference/example. 

1. 8mod_demod.grc : Simple modulator and demodulator for 8 frequencies version, you can observer hopping frequencies in QT GUI sink at end of modulator and final demodulated message at end of demodulator
2. 64mod_demod.grc : The same modulator and demodulator but for 64 frequencies version
3. multipath.grc : GRC file to view performance of FHSS in simulated multipath environment
4. interfrence.grc : GRC file to view performance of FHSS due to in band interferance.

## Troubleshooting :-

1. Compile.sh doesn't work :- Import CMakeList.txt inside the lib folder, and change the names of .cc files to .cpp/.py wherever required. Also, add a blank file blank.cpp in libs/ folder to ensure smooth running. 

2. For including your custom made block in grc, add the path to the config file located at /etc/gnuradio/conf.d and write the path of your "build" directory in the local blocks section in the file.

Then you are good to go :)

## Useful Links for reference:-

http://gnuradio.org/redmine/projects/gnuradio/wiki/Guided_Tutorial_GNU_Radio_in_Python

http://gnuradio.org/redmine/projects/gnuradio/repository/entry/gr-blocks/python/blocks/qa_block_gateway.py
