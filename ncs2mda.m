
    PARAMS.code_base_dir = '/Users/jericcarmichael/Documents/GitHub/vandermeerlab/code-matlab/shared'; % where the codebase repo can be found
%     PARAMS.code_base_dir = 'D:\Users\mvdmlab\My_Documents\GitHub\vandermeerlab\code-matlab\shared';
    addpath(genpath(PARAMS.code_base_dir));
    addpath(genpath('/Users/jericcarmichael/Documents/GitHub/MountainSort-Hackathon-Matlab'))
%     addpath(genpath('D:\Users\mvdmlab\My_Documents\GitHub\MountainSort-Hackathon-Matlab'))
% move to the data

%% add mountainlab
% cd('/Users/jericcarmichael/Documents/GitHub/MountainSort-Hackathon-Matlab/matlab')
run mlsetup.m
cd('/Users/jericcarmichael/Documents/R050-2014-03-28_32ktest')

%%
cfg.ntt_in = 'TT1.ntt';
cfg.ncs_in = 'CSC1.ncs'
[raw, wave]= ConvertNtttoNcs(cfg)





%% get the ncs files
close all
cfg.fc={'tst1.ncs', 'tst2.ncs', 'tst3.ncs', 'tst4.ncs'};
test = LoadCSC(cfg);

data_out = test.data*1000000;

subplot(2,1,1)
plot(data_out(1,:)')

% prepare your MxN array called X %
id = 'raw32_long.mda';
writemda32(data_out,id);

%%
clear data_out
X=readmda(id);
subplot(2,1,2)
plot(X(1,:))