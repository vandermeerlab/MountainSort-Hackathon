%% initalize
    PARAMS.code_base_dir = '/Users/jericcarmichael/Documents/GitHub/vandermeerlab/code-matlab/shared'; % where the codebase repo can be found
    addpath(genpath(PARAMS.code_base_dir));
% move to the data
cd('/Users/jericcarmichael/Documents/R050-2014-03-28_32ktest')
%% load a sample of spikes
% FieldSelectionFlags: Vector with each item being either a zero (excludes
%                          data) or a one (includes data) that determines which
%                          data will be returned for each record. The order of
%                          the items in the vector correspond to the following:
%                             FieldSelectionFlags(1): Timestamps
%                             FieldSelectionFlags(2): Spike Channel Numbers
%                             FieldSelectionFlags(3): Cell Numbers
%                             FieldSelectionFlags(4): Spike Features
%                             FieldSelectionFlags(5): Samples
    fname= 'TT1.ntt';
[Timestamps, ScNumbers, CellNumbers, Features, Samples, Header] =  Nlx2MatSpike(fname, [1 1 1 1 1], 1, 1, [] );

%% check a spike

for ii = 1:4
%     subplot(2,2,ii)
hold on
    plot(Samples(:,ii,3))
end

%% create a test set based on our favourite spike sample
Fs = Header
