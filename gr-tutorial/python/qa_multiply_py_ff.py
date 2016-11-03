#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from multiply_py_ff import multiply_py_ff
import math
import numpy as numpy
class qa_multiply_py_ff (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        src_data = (-3, 4, -5.5, 2, 3,1,1,1,-3, 4, -5.5, 2, 3,1,1,1)
        expected_result = (-6, 8, -11, 4, 6,1,1,1,-3, 4, -5.5, 2, 3,1,1,1)
        src = blocks.vector_source_f (src_data)
        mult = multiply_py_ff()
        dst = blocks.vector_sink_f ()
        self.tb.connect (src, mult)
        self.tb.connect (mult, dst)
        self.tb.run ()
        result_data = dst.data ()
        print "result is " + str(result_data)
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)


if __name__ == '__main__':
    gr_unittest.run(qa_multiply_py_ff, "qa_multiply_py_ff.xml")
