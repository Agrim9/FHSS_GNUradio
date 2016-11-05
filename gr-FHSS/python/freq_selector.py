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
#from gnuradio import blocks

class freq_selector(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="freq_selector",
            in_sig=[np.float32],
            out_sig=[np.float32]
            )
        self.freq = freq = 1000
        self.samp_rate=32000
        self.seed=[1,1,1,1]
        self.update=[0,0,0,0]
        #self.src0= analog.sig_source_f(32000, analog.GR_COS_WAVE, freq, 1)
        print "init"



    def work(self,input_items,output_items):
        out=output_items[0]
        #######
        j=0;
        for i in range(0,len(output_items[0])):
            if j==1000 :
                if self.seed[3] == self.seed[1]:
                    self.update[2]=0
                else:
                    self.update[2]=1
                self.update[1]=self.seed[0]
                self.update[0]=self.seed[3]
                self.update[3]=self.seed[2]
                self.seed=self.update
                self.freq=(self.update[3]*8 + self.update[2]*4 + self.update[1]*2 + self.update[0])*1000
                #Max Freq will be 16 kHz, min 1 KHz
                j=0
            #Now, lowest time period is 62.5 us
            #100 samples every 50us will suffice, thus a delay of 0.5us required
            out[i]=math.cos(2*np.pi*self.freq*i/self.samp_rate)
            time.sleep(0.0001)
            j=j+1
        ###
        return len(output_items[0])
