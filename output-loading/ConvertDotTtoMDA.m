function ConvertDotTtoMDA(cfg_in)
% function ConvertDotTtoMDA(cfg_in)
%
% creates .mda files (one for each tetrode) for all .t files in folder
%

cfg_def.load_questionable_cells = 0; % if 1, include *._t files
cfg_def.nMaxTetrodes = 16; % number of tetrodes to search

cfg = ProcessConfig(cfg_def,cfg_in);

% load files
cfg.fc = FindFiles('*.t');

if cfg.load_questionable_cells
    if cfg.verbose; fprintf('%s: WARNING: loading questionable cells\n',mfun); end
    cfg.fc = cat(1,cfg.fc,FindFiles('*._t'));
end

% iterate over tetrodes
for iTT = 1:cfg_nMaxTetrodes
   
    
    
end
