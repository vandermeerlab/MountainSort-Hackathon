function [csc] =ConvertNtttoNcs(fnames)
%% ConvertNtttoNcs: convert a .ntt discontinuous file into multiple .ncs continously sampled files 



%% default parameters


%% identify channel numbers from ntt

%% extract elements from Ntt file
% for iF = 1:length(fname)
[Timestamps, ScNumbers, CellNumbers, Features, Samples, Header] =  Nlx2MatSpike(fname{iF}, [1 1 1 1 1], 1, 1, [] );



