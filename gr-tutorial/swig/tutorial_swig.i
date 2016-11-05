/* -*- c++ -*- */

#define TUTORIAL_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "tutorial_swig_doc.i"

%{
#include "tutorial/square_ff.h"
%}


%include "tutorial/square_ff.h"
GR_SWIG_BLOCK_MAGIC2(tutorial, square_ff);
