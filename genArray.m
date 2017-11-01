function new_array = genArray(old_array)
% function new_array = genArray(old_array)
% 
% Converts array into 512 row long columns, dropping the samples in the final
% incomplete column
% 
% INPUTS:
% old_array: 1x[] array of samples
% 
% OUTPUTS:
% new_array: 512x[] array of samples

num_rows = length(old_array)/512; % calculate number of columns data fills
round_down = floor(num_rows); % calculate number of complete columns
num_remove = (num_rows - round_down) * 512; % determine leftover in incomplete column
last_data_pt = length(old_array) - num_remove; % find the sample corresponding to the final row in the final complete column
new_array = reshape(old_array(1:last_data_pt),512,[]); % reshape data to 512-row long columns, dropping the final incomplete column