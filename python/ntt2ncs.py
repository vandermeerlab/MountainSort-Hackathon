# -*- coding: utf-8 -*-
"""
Created on Wed Nov 01 13:44:38 2017

@author: Patrick
"""
import numpy as np
import tkFileDialog
import os

def mmap_spike_file(filename): 
    """ Memory map the Neuralynx .ntt file """ 
    #specify the NTT datatypes
    ntt_dtype = np.dtype([ 
        ('timestamp'  , '<u8'), 
        ('sc_number'  , '<u4'), 
        ('cell_number', '<u4'), 
        ('params'     , '<u4',   (8,)),
        ('waveforms'  , '<i2', (32,4)),
    ]) 
    #memmap the file
    mmap = np.memmap(filename, dtype=ntt_dtype, mode='r+', 
       offset=(16 * 2**10))
    
    return mmap['timestamp'],mmap['sc_number'],mmap['cell_number'],mmap['params'],mmap['waveforms']

def stitch_waveforms(waveforms,timestamps):
    
    waveforms = np.swapaxes(waveforms,0,2)
    waveforms = np.swapaxes(waveforms,1,2)
    
    min_timestamp = min(timestamps)
    ntimestamps = timestamps - min_timestamp
    
    sample_rate = 32000
    
    session_length = max(ntimestamps) / 1000000
    session_length *= sample_rate
    session_length = np.int(session_length)
    
    stitched = np.zeros((4,int(session_length)))
        
    for i in range(len(waveforms)):
        for j in range(len(waveforms[0])):
            data = waveforms[i][j]
            ts = ntimestamps[j]
            if int(ts*sample_rate/1000000) + 24 < session_length:
                if ts*sample_rate == 0:
                    start_samp = sample_rate*ts/1000000
                else:
                    start_samp = sample_rate*ts/1000000 - 8
                stitched[i][int(start_samp):int(start_samp+32)] = data
                
    return stitched
            
    
def write_ncs(stitched,ttname,dirname):
        
    ncs_dtype = np.dtype([ 
        ('timestamp'  , '<u8'), 
        ('chan_number'  , '<u4'), 
        ('sample_freq', '<u4'), 
        ('num_valid'     , '<u4'), 
        ('data'  , '<i2', (512,)), 
    ])
    
    for i in range(4):
        filename = dirname + '/' + ttname + '_channel%s.ncs' % str(i+1)
        extracted = np.memmap(filename, dtype=ncs_dtype, mode='w+', 
           offset=(16 * 2**10), shape = len(stitched[i])/512)
        
        for j in range(len(stitched[i])/512):
            timestamp = j*512*32000
            chan_number = i
            sample_freq = 32000
            num_valid = 512
            data = stitched[i][j*512:(j+1)*512]
            
            extracted[j] = (timestamp,chan_number,sample_freq,num_valid,data)
        
        extracted.flush()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
if __name__ == '__main__':        

    filename = tkFileDialog.askopenfilename()
    ttname = os.path.basename(filename)[:3]
    dirname = os.path.dirname(filename)
    timestamps,sc_num,cell_num,params,waveforms = mmap_spike_file(filename)
    stitched = stitch_waveforms(waveforms,timestamps)
    write_ncs(stitched,ttname,dirname)