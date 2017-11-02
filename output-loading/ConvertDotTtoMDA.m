function ConvertDotTtoMDA(cfg_in)
% function ConvertDotTtoMDA(cfg_in)
%
% creates .mda files (one for each tetrode) for all .t files in folder
%

cfg_def.load_questionable_cells = 0; % if 1, include *._t files
cfg_def.nMaxTetrodes = 16; % number of tetrodes to search

cfg = ProcessConfig(cfg_def,cfg_in);

%%
% load files
cfg.fc = FindFiles('*.t');

if cfg.load_questionable_cells
    if cfg.verbose; fprintf('%s: WARNING: loading questionable cells\n',mfun); end
    cfg.fc = cat(1,cfg.fc,FindFiles('*._t'));
end
    
% iterate over possible tetrodes
for iTT = 1:cfg.nMaxTetrodes
    % set proper .t file lookup format
    if iTT < 10
        curr_tNum = ['0' num2str(iTT)];
    else curr_tNum = num2str(iTT);
    end

    % check to see if that tetrode has clusters, if so grab the .t file
    % indices in cfg.fc
    idx_clus = find(cellfun(@(x) any(strfind(x,['TT' curr_tNum])), cfg.fc,'UniformOutput',1));
    if ~isempty(idx_clus)
        disp(['Currently working on TT' curr_tNum]);
        
        % grab a corresponding .ncs file for this tetrode
        ncs_fname = FindFiles(['*CSC' curr_tNum '*.ncs']); 
        ncs_fname = ncs_fname{1};
        [Timestamps,Samples] = Nlx2MatCSC(ncs_fname,[1 0 0 0 1],0,1,1);

        % iterate over clusters
        for iC = 1:length(idx_clus)
            cfg_clus = [];
            cfg_clus.fc = {cfg.fc{idx_clus(iC)}};
            curr_S = LoadSpikes(cfg_clus);
        end
        % ok so i'm completely brain farting here and I had an idea but I
        % completely forgot what I've wanted to do... 
    end
    
    
end
    
end
