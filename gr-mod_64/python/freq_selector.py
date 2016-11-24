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

from gnuradio import analog,blocks,gr
import time
import numpy as np
import math
from scipy.signal import hilbert
import matplotlib.pyplot as plt
#from gnuradio import blocks

class freq_selector(gr.sync_block):
    def __init__(self,samp_rate,sensitivity):
        gr.sync_block.__init__(self,
            name="freq_selector",
            in_sig=[np.float32],
            out_sig=[np.float32]
            )
        self.freq = 6000
        self.samp_rate=samp_rate
        self.sensitivity=sensitivity
        self.num_samples=8192
        self.seed=[1,0,1,1,1,1]
        update=[0,0,0,0,0,0]
        self.freq_seed=[]
        self.freq_sel=0
        #self.src0= analog.sig_source_f(32000, analog.GR_COS_WAVE, freq, 1)
        for i in range((2**len(self.seed))-1):
            power0val=self.seed[5]^self.seed[4]
            update=np.roll(self.seed,1)
            update[0]=power0val
            self.seed=update
            self.freq_seed.append(self.seed)
            #

    def work(self,input_items,output_items):
        in0=input_items[0]
        #######
        ### Preparations
        modulated_signal=[np.complex(math.cos(self.sensitivity*itr),math.sin(self.sensitivity*itr)) for itr in in0]
        M_signal=modulated_signal
        carrier_signal=[]
        self.freq=np.sum([self.freq_seed[self.freq_sel][p]*2**p for p in range(len(self.seed))])*1000 +63000
        #print "frequency-> "+str(self.freq)
        if self.freq_sel == (2**len(self.seed))-2:
            self.freq_sel=0
        else:
            self.freq_sel=self.freq_sel + 1

        C_signal=[np.complex(math.cos(2*np.pi*self.freq*i/self.samp_rate),math.sin(2*np.pi*self.freq*i/self.samp_rate)) for i in range(len(in0))]
        Final_sig=[C_signal[i]*M_signal[i] for i in range(len(in0))]

        output_items[0][:] =np.real(Final_sig)


        #import pdb; pdb.set_trace()
        return len(output_items[0])
