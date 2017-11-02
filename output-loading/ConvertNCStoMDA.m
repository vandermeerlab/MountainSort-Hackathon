function ConvertNCStoMDA(cfg_in)
% function ConvertNCStoMDA(cfg_in)
%
% writes .mda file from .ncs inputs
%
% CONFIG OPTIONS:
%
% cfg_def.fin = {}; % cell array of ncs files
% cfg_def.fout = 'out.mda'; % output filename
%   
% EXAMPLE UASGE:
%
% cfg = []; cfg.fin = {'CSC1.ncs','CSC2.ncs','CSC3.ncs','CSC4.ncs'}; cfg.fout = 'TT1.mda';
% ConvertNCStoMDA(cfg);

cfg_def.fin = {}; % cell array of ncs files
cfg_def.fout = 'out.mda'; % output filename


cfg = ProcessConfig(cfg_def,cfg_in);

temp_out = [];

%% check inputs
if ~iscell(cfg.fin)
    error('Input must be cell array of strings for ncs filenames')
end

%%
for iCSC = length(cfg.fin):-1:1

    this_csc = cfg.fin{iCSC};
    fprintf('Loading file %s (%d/%d)..\n',this_csc,iCSC,length(cfg.fin));

    [Timestamps,Samples] = Nlx2MatCSC(this_csc,[1 0 0 0 1],0,1,1);
    Samples = Samples(:);
    
    temp_out(iCSC,:) = Samples';
    
end

writemda(temp_out,cfg.fout,'int16');