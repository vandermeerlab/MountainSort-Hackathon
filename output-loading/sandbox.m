%% preliminaries

% run MountainSort on the data, this should give you a firings.mda (or
% firings.curated.mda file)

%%
fd = '/home/mvdm/projects/sorting/R050-test2/output/ms3--R050-ds1'; % folder containing firings.mda
fn = 'firings.mda';

%%
cd(fd);
out = readmda(fn);

% need to get tvec