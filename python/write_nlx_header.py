

def write_ntt_header(nlx_headersize=16*2**10, name=None, t_open=None, t_close=None,
                     filetype=None, fileversion=None, recordsize=None,
                     cheetahrev=None, hardwaresubname=None, hardwaresubtype=None,
                     samplingfreq=None, admaxvalue=None, adbitvolts=None,
                     acqentname=None, numadchannels=None, adchannel=None,
                     inputrange=None, inputinverted=None, dsplowcutfilterenabled=None,
                     dsplowcutfreq=None, dsplowcutnumtaps=None, dsplowcutfiltertype=None,
                     dsphighcutfilterenabled=None, dsphighcutfreq=None, dsphighcutnumtaps=None,
                     dsphighcutfiltertype=None, dspdelaycomp=None,
                     dspfilterdelay=None, waveformlen=None, alignmentpt=None,
                     threshval=None, minretriggertime=None, spikeretriggertime=None,
                     dualthresh=None, featurepeak1=None, featurepeak2=None,
                     featurepeak3=None, featurepeak4=None, featurevalley1=None,
                     featurevalley2=None, featurevalley3=None, featurevalley4=None):
    """
    Returns a .ntt header

    Parameters
    ----------
    nlx_headersize: float
        Default is 16*2**10
    name: str
        Default is None
    ...


    Returns
    -------
    header: byte string

    """

    header = '######## Neuralynx Data File Header'
    if name is not None:
        header += '## File Name ' + name
    else:
        header += '## File Name '
    if t_open is not None:
        header += '## Time Opened (m/d/y): ' + t_open
    else:
        header += '## Time Opened (m/d/y): '
    if t_close is not None:
        header += '## Time Closed (m/d/y): ' + t_close
    else:
        header += '## Time Closed (m/d/y): '
    header += '\r\n'
    if filetype is not None:
        header += '-FileType ' + filetype
    else:
        header += '-FileType '
    if fileversion is not None:
        header += '-FileVersion ' + fileversion
    else:
        header += '-FileVersion '
    if recordsize is not None:
        header += '-RecordSize ' + recordsize
    else:
        header += '-RecordSize '
    header += '\r\n'
    if cheetahrev is not None:
        header += '-CheetahRev ' + cheetahrev
    else:
        header += '-CheetahRev '
    header += '\r\n'
    if hardwaresubname is not None:
        header += '-HardwareSubSystemName ' + hardwaresubname
    else:
        header += '-HardwareSubSystemName '
    if hardwaresubtype is not None:
        header += '-HardwareSubSystemType ' + hardwaresubtype
    else:
        header += '-HardwareSubSystemType '
    if samplingfreq is not None:
        header += '-SamplingFrequency ' + samplingfreq
    else:
        header += '-SamplingFrequency '
    if admaxvalue is not None:
        header += '-ADMaxValue ' + admaxvalue
    else:
        header += '-ADMaxValue '
    if adbitvolts is not None:
        header += '-ADBitVolts ' + adbitvolts
    else:
        header += '-ADBitVolts '
    header += '\r\n'
    if acqentname is not None:
        header += '-AcqEntName ' + acqentname
    else:
        header += '-AcqEntName '
    if numadchannels is not None:
        header += '-NumADChannels ' + numadchannels
    else:
        header += '-NumADChannels '
    if adchannel is not None:
        header += 'ADChannel ' + adchannel
    else:
        header += 'ADChannel '
    if inputrange is not None:
        header += '-InputRange ' + inputrange
    else:
        header += '-InputRange '
    if inputinverted is not None:
        header += '-InputInverted ' + inputinverted
    else:
        header += '-InputInverted '
    header += '\r\n'
    if dsplowcutfilterenabled is not None:
        header += '-DSPLowCutFilterEnabled ' + dsplowcutfilterenabled
    else:
        header += '-DSPLowCutFilterEnabled '
    if dsplowcutfreq is not None:
        header += '-DspLowCutFrequency ' + dsplowcutfreq
    else:
        header += '-DspLowCutFrequency '
    if dsplowcutnumtaps is not None:
        header += '-DspLowCutNumTaps ' + dsplowcutnumtaps
    else:
        header += '-DspLowCutNumTaps '
    if dsplowcutfiltertype is not None:
        header += '-DspLowCutFilterType ' + dsplowcutfiltertype
    else:
        header += '-DspLowCutFilterType '
    if dsphighcutfilterenabled is not None:
        header += '-DSPHighCutFilterEnabled ' + dsphighcutfilterenabled
    else:
        header += '-DSPHighCutFilterEnabled '
    if dsphighcutfreq is not None:
        header += '-DspHighCutFrequency ' + dsphighcutfreq
    else:
        header += '-DspHighCutFrequency '
    if dsphighcutnumtaps is not None:
        header += '-DspHighCutNumTaps ' + dsphighcutnumtaps
    else:
        header += '-DspHighCutNumTaps '
    if dsphighcutfiltertype is not None:
        header += '-DspHighCutFilterType ' + dsphighcutfiltertype
    else:
        header += '-DspHighCutFilterType '
    if dspdelaycomp is not None:
        header += '-DspDelayCompensation ' + dspdelaycomp
    else:
        header += '-DspDelayCompensation '
    if dspfilterdelay is not None:
        header += '-DspFilterDelay_us ' + dspfilterdelay
    else:
        header += '-DspFilterDelay_us '
    header += '\r\n'
    if waveformlen is not None:
        header += '-WaveformLength ' + waveformlen
    else:
        header += '-WaveformLength '
    if alignmentpt is not None:
        header += '-AlignmentPt ' + alignmentpt
    else:
        header += '-AlignmentPt '
    if threshval is not None:
        header += '-ThreshVal ' + threshval
    else:
        header += '-ThreshVal '
    if minretriggertime is not None:
        header += '-MinRetriggerSamples ' + minretriggertime
    else:
        header += '-MinRetriggerSamples '
    if spikeretriggertime is not None:
        header += '-SpikeRetriggerTime ' + spikeretriggertime
    else:
        header += '-SpikeRetriggerTime '
    if dualthresh is not None:
        header += '-DualThresholding ' + dualthresh
    else:
        header += '-DualThresholding '
    header += '\r\n'
    if featurepeak1 is not None:
        header += '-Feature Peak ' + featurepeak1
    else:
        header += '-Feature Peak '
    if featurepeak2 is not None:
        header += '-Feature Peak ' + featurepeak2
    else:
        header += '-Feature Peak '
    if featurepeak3 is not None:
        header += '-Feature Peak ' + featurepeak3
    else:
        header += '-Feature Peak '
    if featurepeak4 is not None:
        header += '-Feature Peak ' + featurepeak4
    else:
        header += '-Feature Peak '
    if featurevalley1 is not None:
        header += '-Feature Valley ' + featurevalley1
    else:
        header += '-Feature Valley '
    if featurevalley2 is not None:
        header += '-Feature Valley ' + featurevalley2
    else:
        header += '-Feature Valley '
    if featurevalley3 is not None:
        header += '-Feature Valley ' + featurevalley3
    else:
        header += '-Feature Valley '
    if featurevalley4 is not None:
        header += '-Feature Valley ' + featurevalley4
    else:
        header += '-Feature Valley '
    header += '\r\n'

    offset = int(nlx_headersize - len(header))
    header = header.ljust(offset, '\x00')

    return header.encode()


def write_ncs_header(nlx_headersize=16*2**10, name=None, t_open=None, t_close=None,
                     filetype=None, fileversion=None, recordsize=None,
                     cheetahrev=None, hardwaresubname=None, hardwaresubtype=None,
                     samplingfreq=None, admaxvalue=None, adbitvolts=None,
                     acqentname=None, numadchannels=None, adchannel=None,
                     inputrange=None, inputinverted=None, dsplowcutfilterenabled=None,
                     dsplowcutfreq=None, dsplowcutnumtaps=None, dsplowcutfiltertype=None,
                     dsphighcutfilterenabled=None, dsphighcutfreq=None, dsphighcutnumtaps=None,
                     dsphighcutfiltertype=None, dspdelaycomp=None, dspfilterdelay=None):
    """
    Returns a .ncs header

    Parameters
    ----------
    nlx_headersize: float
        Default is 16*2**10
    name: str
        Default is None
    ...


    Returns
    -------
    header: byte string

    """

    header = '######## Neuralynx Data File Header'
    if name is not None:
        header += '## File Name ' + name
    else:
        header += '## File Name '
    if t_open is not None:
        header += '## Time Opened (m/d/y): ' + t_open
    else:
        header += '## Time Opened (m/d/y): '
    if t_close is not None:
        header += '## Time Closed (m/d/y): ' + t_close
    else:
        header += '## Time Closed (m/d/y): '
    header += '\r\n'
    if filetype is not None:
        header += '-FileType ' + filetype
    else:
        header += '-FileType '
    if fileversion is not None:
        header += '-FileVersion ' + fileversion
    else:
        header += '-FileVersion '
    if recordsize is not None:
        header += '-RecordSize ' + recordsize
    else:
        header += '-RecordSize '
    header += '\r\n'
    if cheetahrev is not None:
        header += '-CheetahRev ' + cheetahrev
    else:
        header += '-CheetahRev '
    header += '\r\n'
    if hardwaresubname is not None:
        header += '-HardwareSubSystemName ' + hardwaresubname
    else:
        header += '-HardwareSubSystemName '
    if hardwaresubtype is not None:
        header += '-HardwareSubSystemType ' + hardwaresubtype
    else:
        header += '-HardwareSubSystemType '
    if samplingfreq is not None:
        header += '-SamplingFrequency ' + samplingfreq
    else:
        header += '-SamplingFrequency '
    if admaxvalue is not None:
        header += '-ADMaxValue ' + admaxvalue
    else:
        header += '-ADMaxValue '
    if adbitvolts is not None:
        header += '-ADBitVolts ' + adbitvolts
    else:
        header += '-ADBitVolts '
    header += '\r\n'
    if acqentname is not None:
        header += '-AcqEntName ' + acqentname
    else:
        header += '-AcqEntName '
    if numadchannels is not None:
        header += '-NumADChannels ' + numadchannels
    else:
        header += '-NumADChannels '
    if adchannel is not None:
        header += 'ADChannel ' + adchannel
    else:
        header += 'ADChannel '
    if inputrange is not None:
        header += '-InputRange ' + inputrange
    else:
        header += '-InputRange '
    if inputinverted is not None:
        header += '-InputInverted ' + inputinverted
    else:
        header += '-InputInverted '
    header += '\r\n'
    if dsplowcutfilterenabled is not None:
        header += '-DSPLowCutFilterEnabled ' + dsplowcutfilterenabled
    else:
        header += '-DSPLowCutFilterEnabled '
    if dsplowcutfreq is not None:
        header += '-DspLowCutFrequency ' + dsplowcutfreq
    else:
        header += '-DspLowCutFrequency '
    if dsplowcutnumtaps is not None:
        header += '-DspLowCutNumTaps ' + dsplowcutnumtaps
    else:
        header += '-DspLowCutNumTaps '
    if dsplowcutfiltertype is not None:
        header += '-DspLowCutFilterType ' + dsplowcutfiltertype
    else:
        header += '-DspLowCutFilterType '
    if dsphighcutfilterenabled is not None:
        header += '-DSPHighCutFilterEnabled ' + dsphighcutfilterenabled
    else:
        header += '-DSPHighCutFilterEnabled '
    if dsphighcutfreq is not None:
        header += '-DspHighCutFrequency ' + dsphighcutfreq
    else:
        header += '-DspHighCutFrequency '
    if dsphighcutnumtaps is not None:
        header += '-DspHighCutNumTaps ' + dsphighcutnumtaps
    else:
        header += '-DspHighCutNumTaps '
    if dsphighcutfiltertype is not None:
        header += '-DspHighCutFilterType ' + dsphighcutfiltertype
    else:
        header += '-DspHighCutFilterType '
    if dspdelaycomp is not None:
        header += '-DspDelayCompensation ' + dspdelaycomp
    else:
        header += '-DspDelayCompensation '
    if dspfilterdelay is not None:
        header += '-DspFilterDelay_us ' + dspfilterdelay
    else:
        header += '-DspFilterDelay_us '
    header += '\r\n'

    offset = int(nlx_headersize - len(header))
    header = header.ljust(offset, '\x00')

    return header.encode()
