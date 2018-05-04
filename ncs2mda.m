
    PARAMS.code_base_dir = '/Users/jericcarmichael/Documents/GitHub/vandermeerlab/code-matlab/shared'; % where the codebase repo can be found
%     PARAMS.code_base_dir = 'D:\Users\mvdmlab\My_Documents\GitHub\vandermeerlab\code-matlab\shared';
    addpath(genpath(PARAMS.code_base_dir));
    addpath(genpath('/Users/jericcarmichael/Documents/GitHub/MountainSort-Hackathon-Matlab'))
%     addpath(genpath('D:\Users\mvdmlab\My_Documents\GitHub\MountainSort-Hackathon-Matlab'))
% move to the data
cd('/Users/jericcarmichael/Documents/R050-2014-03-28_32ktest')

%% add mountainlab
cd('/Users/jericcarmichael/Documents/GitHub/mountainsort/matlab')
run mlsetup.m

%% get the ncs files
cfg.fc={'test1.ncs', 'test2.ncs', 'test3.ncs', 'test4.ncs'};
test = LoadCSC(cfg);

data_out = test.data;



% prepare your MxN array called X %

writemda16i(data_out,'raw2.mda');