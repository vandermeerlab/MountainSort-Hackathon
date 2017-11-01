function S = LoadMountainSortFirings(cfg_in)
% function S = LoadMountainSortFirings(cfg_in)
%
% Load MountainSort output (firings.mda) into ts
%
% MvdM 2017-11-01 initial version

cfg_def.fn = 'firings.mda';

cfg = ProcessConfig(cfg_def,cfg_in);

if ~isfield(cfg,'fd')
   error('Must specify MountainSort output folder as cfg.fd'); 
end

cd(cfg.fd);
out = readmda(cfg.fn);

% need to get tvec -- so first find out filename of original
fh = fopen('raw.mda.prv');
jd = jsondecode(fscanf(fh,'%s'));

orig_fp = regexprep(jd.original_path,'.mda','.ncs');
[fp,fn,fe] = fileparts(orig_fp);

pushdir(fp);
%please = []; please.fc{1} = cat(2,upper(fn),fe); % use if you changed filename case when converting 
please = []; please.fc{1} = cat(2,fn,fe);

try
    csc = LoadCSC(please);
catch
    error('Could not locate original file %s',please.fc{1});
end
popdir;

spk_idxs = out(2,:);
clu_ids = out(3,:);

nCells = max(clu_ids);

S = ts;
for iC = 1:nCells
   
    this_idx = spk_idxs(clu_ids == iC);
    this_t = csc.tvec(this_idx);
    S.t{iC} = this_t;
    
end