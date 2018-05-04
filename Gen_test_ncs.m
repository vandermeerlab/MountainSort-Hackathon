%% initalize
    PARAMS.code_base_dir = '/Users/jericcarmichael/Documents/GitHub/vandermeerlab/code-matlab/shared'; % where the codebase repo can be found
%     PARAMS.code_base_dir = 'D:\Users\mvdmlab\My_Documents\GitHub\vandermeerlab\code-matlab\shared';
    addpath(genpath(PARAMS.code_base_dir));
    addpath(genpath('/Users/jericcarmichael/Documents/GitHub/MountainSort-Hackathon-Matlab'))
%     addpath(genpath('D:\Users\mvdmlab\My_Documents\GitHub\MountainSort-Hackathon-Matlab'))
% move to the data
cd('/Users/jericcarmichael/Documents/R050-2014-03-28_32ktest')
% cd('D:\DATA\R050-2014-03-28_32ktest')
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
[~, ~, ~, ~, ~, Header_temp] = Nlx2MatCSC('CSC1.ncs', [1 1 1 1 1], 1, 1, [] ); % use this to get a header template

%% check a spike

for ii = 1:4
    %     subplot(2,2,ii)
    hold on
    plot(Samples(:,ii,3))
end

%% create a test set based on our favourite spike sample
Fs = 320000;   %Header   % YOUKI make this into a regexp kinda search thing or something
t_len = 120;   % time in sec

test.tvec = 0:1/Fs:t_len;
test.data = zeros(4,length(test.tvec));

% put spikes into ncell X tvec array at fixed number and freq
rng(0,'twister');
n=500;
xend = length(test.tvec);
S_ts=1+rand(1,n)*(xend-1);
S_ts = sort(round(S_ts));
% check for overlaps within a fixed time window (in this case the number of
% samples in a spike sample (32)).
for ii = 1:n-1
    if S_ts(ii+1) - S_ts(ii) < 32;
        flags(ii) = 1;
    else
        flags(ii) = 0;
    end
end
if sum(flags) <0
    disp('OVERLAP')
end

for ii = 1:length(S_ts)
    test.data(1,S_ts(ii):S_ts(ii)+31) = Samples(:,1,3)';
    test.data(2,S_ts(ii):S_ts(ii)+31) = Samples(:,2,3)';
    test.data(3,S_ts(ii):S_ts(ii)+31) = Samples(:,3,3)';
    test.data(4,S_ts(ii):S_ts(ii)+31) = Samples(:,4,3)';
end
%% plot the test data
figure(100)
subplot(1,4,1:3)
hold on
plot(test.tvec, test.data)

%% try to get N valid samples
[Timestamps, ChannelNumbers, SampleFrequencies, NumberOfValidSamples, Samples, Header_out] = Nlx2MatCSC('CSC1.ncs', [1 1 1 1 1], 1, 1, [] );
Mat2NlxCSC('test.ncs', 0, 1, 1, [1 1 1 1 1 1], Timestamps, ChannelNumbers, SampleFrequencies, NumberOfValidSamples,Samples, Header);

nel = numel(Samples);
smpls = nel/512;
check = length(Timestamps);
smpls == check

%% put into .ncs
Timestamps_out = (test.tvec .*512)./10^-6;
nSample = floor(length(test.tvec)/512);
NumberOfValidSamples_out = repmat(512, 1,nSample);
SampleFrequencies_out = repmat(Fs,1,nSample);
ChannelNumbers_out = zeros(1,nSample);
Header_out = Header_temp;
for iCh = 1:size(test.data,1)
    Samples_out = genArray(test.data(iCh,:));
    s_idx = strfind(Header_temp{18},'CSC');
    Header_out{18} =[Header_temp{18}(1:s_idx-1) 'test' num2str(iCh)]; 
    Mat2NlxCSC(['tst' num2str(iCh) '.ncs'], 0, 1, 1, [1 1 1 1 1 1], Timestamps_out, ChannelNumbers_out,SampleFrequencies_out , NumberOfValidSamples_out,Samples_out, Header_out);
end





