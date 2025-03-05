clear all

% run_start is always first, then pupil, then whisker, and laser the last (after param.prestim_time)

param = {};

%% set it first
param.mouse = '1120293'
param.test = 'test1_LHb_PMnR'
mouse_num = [param.mouse,'_',param.test];
param.date = datestr(now,'hhMMss_ddmmyy')
param.lase_actual_start_from_movie = [342,11.4000];
%%

% laser protocol
param.prestim_time = 15;
param.laser_on = 3;
param.laser_off = 12;
param.laserlevel = 20;
param.freq = 20;
param.repeat_num = 30; % default 30

s2 = serial('COM9','BaudRate',9600,'Terminator','CR/LF'); % usb port for laser


%% Construct VideoWriter object and set Disk Logger Property
timenow = datestr(now,'hhMMss_ddmmyy');

dq = daq("ni");
dq.Rate = 1000;
ch_a0=addinput(dq,"NIDAQ_run","ai0","Voltage");


%%

start(dq,"NumScans",floor((param.prestim_time+(param.laser_on+param.laser_off)*param.repeat_num+5))*dq.Rate);
clock_run_start = clock;

fopen(s2);
t2 = tic;
clock_laser_start = clock;

com_py = 'python C:\Users\Kelly_group03\PycharmProjects\camera_maybe\x2.py'; % python movie capture
[status,com_out] = system(com_py);

clock_pupil_whisker_start = clock;
t1 = tic;
run_data = [];
pause(param.prestim_time)

param.clock_pupil_whisker_start = clock_pupil_whisker_start;
param.clock_laser_start = clock_laser_start;
param.clock_run_start = clock_run_start;
pause(5)
% scanData = read(dq,seconds(5));
% run_data = [run_data;scanData.NIDAQ_run_ai0];
display('stop the movies by pressing q')
elapsedTime1 = toc(t1);

scanData = read(dq,"all");
run_data = scanData.NIDAQ_run_ai0;
save(['run_',mouse_num,'_',timenow,'.mat'],'run_data')


%%

fclose(s2);
param.movies_start = t1;
param.laser_start = t2;
save([mouse_num,'_',timenow,'_laser_movieinfo.mat'],'param')

