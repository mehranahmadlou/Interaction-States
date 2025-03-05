clear all

mouse_num = '1118244_test1';

% run_start is always first, then pupil, then whisker, and laser the last (after param.prestim_time)

param = {};

% laser protocol
param.prestim_time = 15;
param.laser_on = 0.01;
param.laser_off = 15;
param.laser_off_duration = param.laser_off - (param.laser_on + 3);
param.laser_on_duration = (param.laser_on + 3);
param.laserlevel = 20;
param.freq = 20;
param.repeat_num = 20;

s2 = serial('COM9','BaudRate',9600,'Terminator','CR/LF'); % usb port for laser

vid1 = videoinput('winvideo', 2, 'Y800_320x240');
vid2 = videoinput('winvideo', 1, 'Y800_320x240');
src1 = getselectedsource(vid1);
src2 = getselectedsource(vid2);

% vid1.FramesPerTrigger = Inf;

% vid1.TimeOut = Inf;
vid1.FrameGrabInterval = 1;
vid1.LoggingMode = 'disk&memory';
vid1.FramesPerTrigger = 1;
vid1.TriggerRepeat = Inf;

vid2.FrameGrabInterval = 1;
vid2.LoggingMode = 'disk&memory';
vid2.FramesPerTrigger = 1;
vid2.TriggerRepeat = Inf;

w = webcamlist;  % 'DMK 23UV024'
cam_pupil = webcam(w{1}); % 'DMK 22BUC03'
cam_whisker = webcam(w{2});  % 'DMK 23UV024'
cam_pupil.Resolution = '320x240';
cam_whisker.Resolution = '320x240';


img1 = snapshot(cam_pupil);
img2 = snapshot(cam_whisker);

imshow(img1)
h1 = drawrectangle;
wait(h1);
vid1.ROIPosition = h1.Position;
close

imshow(img2)
h2 = drawrectangle;
wait(h2);
vid2.ROIPosition = h2.Position;
close

clear cam_pupil
clear cam_whisker

%% Construct VideoWriter object and set Disk Logger Property
timenow = datestr(now,'hhMMss_ddmmyy');

dq = daq("ni");
dq.Rate = 1000;
ch_a0=addinput(dq,"NIDAQ_run","ai0","Voltage");

v1 = VideoWriter(['pupil_',mouse_num,'_',timenow,'.avi']);
v1.FrameRate = 30;
v1.Quality = 50;
vid1.DiskLogger = v1;
% vid1.SelectedSourceName = 'input1';
v2 = VideoWriter(['whisker_',mouse_num,'_',timenow,'.avi']);
v2.FrameRate = 30;
v2.Quality = 50;
vid2.DiskLogger = v2;

%%

preview(vid1);
% preview(vid2);

start(dq,"NumScans",(param.prestim_time+(param.laser_on+param.laser_off)*param.repeat_num+5)*dq.Rate);
clock_run_start = clock;

start(vid1);
% t4 = tic;
clock_pupil_start = clock;
t1 = tic;

start(vid2);
clock_whisker_start = clock;
t2 = tic;
% stoppreview(vid);
run_data = [];
pause(param.prestim_time)
% elapsedTime4 = toc(t4);
% scanData = read(dq,seconds(elapsedTime4));
% run_data = [run_data;scanData.NIDAQ_run_ai0];
TT = [];
TTend = [];
clock_laser_start = clock;
for  i = 1:param.repeat_num
    fopen(s2);
    tt = tic;
    pause(param.laser_on)
    fclose(s2);
    pause(param.laser_off)
    TT = [TT,tt];
    TTend = [TTend,toc(tt)];
%     elapsedTime3 = toc(t3);
%     scanData = read(dq,seconds(elapsedTime3));
%     run_data = [run_data;scanData.NIDAQ_run_ai0];
end
param.laser_trig = TT;
param.laser_actual_dur = TTend;
param.clock_pupil_start = clock_pupil_start;
param.clock_whisker_start = clock_whisker_start;
param.clock_laser_start = clock_laser_start;
param.clock_run_start = clock_run_start;
pause(5)
% scanData = read(dq,seconds(5));
% run_data = [run_data;scanData.NIDAQ_run_ai0];

stoppreview(vid1);
stop(vid1);
elapsedTime1 = toc(t1);
stoppreview(vid2);
stop(vid2);
elapsedTime2 = toc(t2);

scanData = read(dq,"all");
run_data = scanData.NIDAQ_run_ai0;
save(['run_',mouse_num,'_',timenow,'.mat'],'run_data')
%% Option 1 to save the movie

% diskLogger = VideoWriter('C:\Matlab\Webcam_Pupil_Laser\xxx.avi', 'Grayscale AVI');
% open(diskLogger);
% data = getdata(vid, vid1.FramesAvailable);
% numFrames = size(data, 4);
% for ii = 1:numFrames
%     writeVideo(diskLogger, data(:,:,:,ii));
% end
% close(diskLogger);

%%
% Compute actual Frame Rate



framesaq1 = vid1.FramesAcquired;
ActualFR1 = framesaq1/elapsedTime1;
delete(vid1);
name_pupil = ['pupil_',mouse_num];
% ChangeFrameRate(['pupil_',mouse_num,'_',timenow,'.avi'], name_pupil, timenow, ActualFR1)
param.ActualFR_pupil = ActualFR1;

framesaq2 = vid2.FramesAcquired;
ActualFR2 = framesaq2/elapsedTime2;
delete(vid2);
name_whisker = ['whisker_',mouse_num];
% ChangeFrameRate(['whisker_',mouse_num,'_',timenow,'.avi'], name_whisker, timenow, ActualFR2)
param.ActualFR_whisker = ActualFR2;
param.pupilstart = t1;
param.whiskerstart = t2;
save([mouse_num,'_',timenow,'_laser_movieinfo.mat'],'param')

%% This function changes the Frame Rate that the Saved Video is as long as the recording
function ChangeFrameRate(Video, name_type, timestr, ActualFR)
% Construct Video Objects
vidObj = VideoReader(Video);
writerObj = VideoWriter(['ActualFR_', name_type, timestr,'.avi']);
writerObj.FrameRate = ActualFR;
writerObj.Quality = 50;
% Open Video Writer Object
open(writerObj);
% Read video frames until the end of the file is reached
while hasFrame(vidObj)
    vidFrame = readFrame(vidObj);
    writeVideo(writerObj, vidFrame)
    pause(1/vidObj.FrameRate);
end
% Close Video Writer Object
close(writerObj);
end