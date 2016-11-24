# FHSS_GNUradio
Building a block to implement FHSS in GNUradio

Pre-Requisite Libraries :-

  1. sudo apt-get install liblog4cpp5-dev
  2. sudo apt-get install swig
  3. sudo apt-get install doxygen
  4. sudo apt-get install libcppunit-dev
  5. sudo apt-get install cppunit
  6. sudo apt-get install cppunit-dev
  7. sudo apt-get install gnuradio-dev

Import CMakeList.txt inside the lib folder, and change the names of .cc files to .cpp/.py wherever required. Also, add a blank file blank.cpp in libs/ to ensure smooth running. Add blank.cpp wherever in the CMakeLists.txt too (or just import from mine)

For including your custom made block in grc, add the path to the config file located at /etc/gnuradio/conf.d and write the path of your "build" directory in the local blocks section in the file.

Then you are good to go :)

Useful Links for reference:-

http://gnuradio.org/redmine/projects/gnuradio/wiki/Guided_Tutorial_GNU_Radio_in_Python

http://gnuradio.org/redmine/projects/gnuradio/repository/entry/gr-blocks/python/blocks/qa_block_gateway.py
