% first run 'webcam_Python_laser_pupil_whisker.m' with 2 repeats
v = VideoReader('Pupil.avi');
x = [];
for i = 1:500; frame = read(v,i);X = frame(:,:,3);x = [x,max(X(:))];end;
figure;plot(x)
% mouse_num test 1 1118855
% x0 11.2667 52

% x1 11.6000 344

% x2 11.5333 346

% x4 11.4667 344
% x5 11.5333 346
% x6 11.5333 346

% 337
% 338
% 338


% 337
% 338
% 336
% 336
% 339


% 343
% 342
% 340
% 340
% 343


% 344
% 342
