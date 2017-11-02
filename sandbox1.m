%% Generate an arbitrary 

cd('/Users/youkitanaka/Desktop/R050-2014-03-28_32ktest')
fname= 'TT1.ntt';
[Timestamps, ScNumbers, CellNumbers, Features, Samples, Header] =  Nlx2MatSpike(fname, [1 1 1 1 1], 1, 1, [] );


regexp([Header{:}],'(?<=SamplingFrequency[^0-9]*)[0-9]*','match')




%% testing some ncs to mda stuff

% the first four bytes that specify the data format
% fwrite(FF,-3,'int32');

% the second four bytes that specify the number of bytes in each entry 
% fwrite(FF,4,'int32');

% the third four bytes that specify the number of dimensions (
% fwrite(FF,num_dims,'int32');

% dimprod=1;

% for dd=1:num_dims
%     fwrite(FF,size(X,dd),'int32');
%     dimprod=dimprod*size(X,dd);
% end;

% Y=reshape(X,dimprod,1);

% fwrite(FF,Y,'float32');

%%
cd('/Users/youkitanaka/Desktop/R050-2014-03-28_32ktest')
                                 
                               