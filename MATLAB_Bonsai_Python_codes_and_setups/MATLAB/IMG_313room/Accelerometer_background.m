dq = daq("ni");
dq.Rate = 2000;
a=addinput(dq,"NIDAQ_run","ai0","Voltage");
dq.ScansAvailableFcnCount = 2000;
Data = [];
Tstamps = [];
for i=1:5
start(dq, "Duration", seconds(1))
[data, timestamps, ~] = read(dq, dq.ScansAvailableFcnCount, "OutputFormat", "Matrix");
Data = [Data;data];
Tstamps = [Tstamps;timestamps];
end
stop(dq)


%%
clear
session = daq.createSession('ni');
session.Rate=2000;
% session.IsContinuous = true;
addAnalogInputChannel(session,'NIDAQ_run', 0 , 'Voltage'); 
session.DurationInSeconds = 3600; %3600; % 1 hr
prepare(session)
data = start(dq);
save(['C:\Matlab\Webcam_Pupil_Laser','\nose_poke.mat'],'data')
%%


% function [data, timestamps] = plotDataAvailable(src, ~)
%     [data, timestamps, ~] = read(src, src.ScansAvailableFcnCount, "OutputFormat", "Matrix");
%     plot(timestamps, data);
% end