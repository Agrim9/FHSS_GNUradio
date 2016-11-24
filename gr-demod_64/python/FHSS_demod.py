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
import matplotlib.pyplot as plt
import math
import sys
from scipy.fftpack import fft
from scipy.signal import freqz, hilbert

class FHSS_demod(gr.sync_block):
    """
    docstring for block FHSS_demod
    """
    def __init__(self,samp_rate):
        gr.sync_block.__init__(self,
            name="FHSS_demod",
            in_sig=[np.float32],
            out_sig=[np.float32]
            )
        self.samp_rate=samp_rate
        self.num_samples=1168
        #self.gnu_buff=8192
        self.seed=[1,1,1,1,1,1]
        update=[0,0,0,0,0,0]
        #self.buffer=[]
        self.index=0
        self.strt=1
        self.counter=630
        self.threshold = 0.8 #### IMPORTANT
        self.freq_seed=[]
        self.acq=0
        self.track_freq=6000
        for i in range((2**len(self.seed))-1):
            power0val=self.seed[5]^self.seed[4]
            update=np.roll(self.seed,1)
            update[0]=power0val
            self.seed=update
            self.freq_seed.append(self.seed)
        ###
    def work(self, input_items, output_items):
        in0 = input_items[0]
        # <+signal processing here+>
        if((self.strt==1) or (self.counter==0)):
            #########  HOPPING FOR DEMODULATION ###############
            self.index=self.index+1
            self.num_samples=int(len(in0)/63)
            hop_carrier=[]
            hopped_ct=[]
            for seed_freq in self.freq_seed:
                rx_frequency=np.sum([seed_freq[i]*2**i for i in range(len(self.seed))])*1000 +63000
                hop_carrier=[np.complex(math.cos(2*np.pi*rx_frequency*i/self.samp_rate),math.sin(2*np.pi*rx_frequency*i/self.samp_rate)) for i in range(self.num_samples)]
                hopped_ct.append(hop_carrier)

            ################################################
            ######### Multiply with input signal ###########
            analytic_signal=hilbert(in0)
            if(len(hopped_ct)>0):
                corr_signal=hopped_ct
            else:
                corr_signal=[]
            lpf_out=[np.real(analytic_signal[ctr*self.num_samples:(ctr+1)*self.num_samples]*np.conj(corr_signal[ctr])) for ctr in range(63)]
            ##################################################
            ############# SQUARED WAVEFORM ####################
            square_out=[[t*t for t in i] for i in lpf_out]
            ##################################################
            #Uncomment comments for verification
            ############ ACQUISITION SYSTEM ##################
            integrated_out=[np.sum(m[1:self.num_samples])/self.num_samples for m in square_out]
            print"Length" +str(len(integrated_out))
            #import pdb; pdb.set_trace()
            #print "Integrated output " + str(["%.2f" % i for i in integrated_out])
            #acquired_freq_index= [i  for i,j in enumerate(integrated_out) if (j>=self.threshold and j==max(integrated_out))]
            acquired_freq_index= [i  for i,j in enumerate(integrated_out) if (j>=self.threshold and j==max(integrated_out))]
            ## indices in freq can be one or more !!!!
            if len(acquired_freq_index) == 0:
                freq_tracked=[0,0,-1]
                self.acq=0
            else:
                freq_tracked=self.freq_seed[acquired_freq_index[0]]
                self.track_freq=freq_tracked
                self.acq=1

            ###############################################
            ############# Tracking strts Now #############

            #Periodic Counter of 70 freq to be strted upon aquisiton, then to be strted again
            if self.acq == 1:
                index2=acquired_freq_index[0]
                tr_freq=np.sum([freq_tracked[i]*2**i for i in range(len(self.seed))])*1000 + 63000
                print "Tracked Frequency is " + str(tr_freq)
                tr_i_wave=[math.cos(2*np.pi*tr_freq*it/self.samp_rate) for it in range(0,len(in0))]
                self.strt=0
                self.counter=70
                tr_signal=hilbert(tr_i_wave)
                analytic_signal=hilbert(in0)
                X_signal=analytic_signal*np.conj(tr_signal)     ## removed Carrier
                ## Extract message from argument
                msg_signal=np.imag(np.log(X_signal))
                output_items[0][:]=msg_signal[:len(in0)]
                #import pdb; pdb.set_trace()
                #print "Buffer length is " +str(len(output_items[1]))
                return (len(output_items[0]))

        else:
            self.counter=self.counter-1
            power0val=self.track_freq[5]^self.track_freq[4]
            upd=np.roll(self.track_freq,1)
            upd[0]=power0val
            self.track_freq=upd
            tr_freq=np.sum([self.track_freq[i]*2**i for i in range(len(self.seed))])*1000 +63000
            tr_i_wave=[math.cos(2*np.pi*tr_freq*it/self.samp_rate) for it in range(0,len(in0))]
            tr_signal=hilbert(tr_i_wave)
            analytic_signal=hilbert(in0)
            X_signal=analytic_signal*np.conj(tr_signal)     ## removed Carrier
            ## Extract message from argument
            msg_signal=np.imag(np.log(X_signal))
            output_items[0][:]=msg_signal[:len(in0)]
            #import pdb; pdb.set_trace()
            #print "Buffer length is " +str(len(output_items[1]))

        return (len(output_items[0]))
