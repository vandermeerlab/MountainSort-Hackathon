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
    
    #return the data
    return mmap['timestamp'],mmap['sc_number'],mmap['cell_number'],mmap['params'],mmap['waveforms']

def stitch_waveforms(waveforms,timestamps):
    """ stitch the waveforms into one array """
    
    #swap some axes to make the data more intuitive
    waveforms = np.swapaxes(waveforms,0,2)
    waveforms = np.swapaxes(waveforms,1,2)
    
    #change the timestamps to start at zero
    min_timestamp = min(timestamps)
    ntimestamps = timestamps - min_timestamp
    
    #figure out the session length in samples
    sample_rate = 32000
    session_length = max(ntimestamps) / 1000000
    session_length *= sample_rate
    session_length = np.int(session_length)
    
    #start an array of zeros, one dimension for channels and one for samples
    stitched = np.zeros((4,int(session_length)))
        
    #for each channel...
    for i in range(len(waveforms)):
        #for each spike on this channel...
        for j in range(len(waveforms[0])):
            #grab our spike data
            data = waveforms[i][j]
            #figure out which sample number we need to insert at to 
            #preserve timestamp validity
            ts = ntimestamps[j]
            if int(ts*sample_rate/1000000) + 24 < session_length:
                if ts*sample_rate == 0:
                    start_samp = sample_rate*ts/1000000
                else:
                    start_samp = sample_rate*ts/1000000 - 8
                #add the data
                stitched[i][int(start_samp):int(start_samp+32)] = data
    #return it  
    return stitched
            
    
def write_ncs(stitched,ttname,dirname):
    """ write our zero-padded waveforms to ncs files """
    
    #define out ncs datatypes
    ncs_dtype = np.dtype([ 
        ('timestamp'  , '<u8'), 
        ('chan_number'  , '<u4'), 
        ('sample_freq', '<u4'), 
        ('num_valid'     , '<u4'), 
        ('data'  , '<i2', (512,)), 
    ])
    
    #for each channel...
    for i in range(4):
        #decide our new filename
        filename = dirname + '/' + ttname + '_channel%s.ncs' % str(i+1)
        #make the new file
        extracted = np.memmap(filename, dtype=ncs_dtype, mode='w+', 
           offset=(16 * 2**10), shape = len(stitched[i])/512)
        
        #for each chunk of 512 samples...
        for j in range(len(stitched[i])/512):
            #grab appropriate data
            timestamp = j*1000000*512/32000
            chan_number = i
            sample_freq = 32000
            num_valid = 512
            data = stitched[i][j*512:(j+1)*512]
            
            #write the data to file
            extracted[j] = (timestamp,chan_number,sample_freq,num_valid,data)
        
        #flush the changes to disk
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