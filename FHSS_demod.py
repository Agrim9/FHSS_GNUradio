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

import numpy as np
from gnuradio import gr
import math
from scipy.signal import butter, lfilter, freqz

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

class FHSS_demod(gr.sync_block):
    """
    docstring for block FHSS_demod
    """
    def __init__(self,samp_rate):
        gr.sync_block.__init__(self,
            name="FHSS_demod",
            in_sig=[np.complex64],
            out_sig=[np.complex64,np.complex64])
        self.samp_rate=samp_rate
        self.num_samples=575
        self.gnu_buff=4095
        self.seed=[1,1,1]
        update=[0,0,0]
        self.buffer=[]
        self.index=0
        self.threshold = 0.40 #### IMPORTANT
        self.freq_seed=[]
        self.acq=0
        for i in range((2**len(self.seed))-1):
            power0val=self.seed[2]^self.seed[1]
            update=np.roll(self.seed,1)
            update[0]=power0val
            self.seed=update
            self.freq_seed.append(self.seed)
        ###
    def work(self, input_items, output_items):
        complx_in = input_items[0]
        out = output_items[0]
        out0 = output_items[1]
        # <+signal processing here+>
        in0=complx_in.real
        self.index=self.index+1
        if len(self.buffer) == 0:
            if len(in0) >= self.gnu_buff:
                in1=in0
            else:
                self.buffer=in0
                in1=[0 for i in range(self.gnu_buff)]
        else:
            if len(self.buffer)+len(in0) >= self.gnu_buff:
                in1=np.append(self.buffer,in0[0:(self.gnu_buff-len(self.buffer))])
                self.buffer=in0[self.gnu_buff-len(self.buffer):len(in0)]
            else:
                self.buffer=np.append(self.buffer,in0)
                in1=[0 for i in range(self.gnu_buff)]
        #print "in1 sum " + str(sum(in1))
        #########  HOPPING FOR DEMODULATION ###############
        hop_carrier=[]
        freq_i=1
        j=0
        rx_frequency=6000
        for i in range(0,len(in1)):   ### changed from range(len(output_items[0])) ###size 8192
            if j==self.num_samples :            ## 1170 here
                rx_frequency=np.sum([self.freq_seed[freq_i][p]*2**p for p in range(len(self.seed))])*1000
                if freq_i == ((2**len(self.seed))-2) :
                    freq_i=0
                else:
                    freq_i=freq_i+1
                j=0
            j=j+1
            hop_carrier.append(math.cos(2*np.pi*rx_frequency*i/self.samp_rate))
            #
        print "Sum HC is " + str(sum(hop_carrier))
        print "Hop Carrier Length" + str(len(hop_carrier))
        for i in range(64):
            hop_carrier.append(0)
        ################################################
        ######### Multiply with input signal ###########
        mult_out=[(in1[ip])*(hop_carrier[ip]) for ip in range(self.gnu_buff)]
        import pdb; pdb.set_trace()
        print "Sum MO is " + str(sum(mult_out))
        ################################################
        ########### LOW PASS FILTER #####################
        delta2=1.0/self.samp_rate
        order = 6
        fs = self.samp_rate       # sample rate, Hz
        cutoff = 500  # desired cutoff frequency of the filter, Hz
        y = butter_lowpass_filter(mult_out, cutoff, fs, order)
        lpf_out=y[:self.gnu_buff]
        print "LPF out"
        print ["%.2f" % i for i in lpf_out[1:40]]
        ##################################################
        ############# SQUARED WAVEFORM ####################
        square_out=[4*i*i for i in lpf_out]
        ##################################################
        #Uncomment comments for verification
        ############ ACQUISITION SYSTEM ##################
        integrated_out=[np.sum(square_out[i*self.num_samples:(i+1)*self.num_samples])/self.num_samples for i in range(7)]
        #print "Integration "
        print "Integrated output " + str(["%.2f" % i for i in integrated_out])
        acquired_freq_index= [i  for i,j in enumerate(integrated_out) if (j>=self.threshold and j==max(integrated_out))]
          ## indices in freq can be one or more !!!!

        if len(acquired_freq_index) == 0:
            freq_tracked=[0,0,-1]
            self.acq=0
        else:
            freq_tracked=self.freq_seed[acquired_freq_index[0]]        ### gives the freq seed value
            #print integrated_out[acquired_freq_index[0]]
            self.acq=1
        ###############################################
        ############# Tracking Starts Now #############
        print "Frequency tracked is " + str(freq_tracked)
        if self.acq == 1:
            jt=0
            index2=acquired_freq_index[0]
            tr_freq=np.sum([freq_tracked[i]*2**i for i in range(len(self.seed))])*1000
            for it in range(0,len(output_items[1])):
                out0[it]=np.complex(math.cos(2*np.pi*tr_freq*it/self.samp_rate),math.sin(2*np.pi*tr_freq*it/self.samp_rate))
        else:
            out0[:]=0
        out = complx_in
        print "Buffer length is " +str(len(output_items[1]))
        return len(output_items)
