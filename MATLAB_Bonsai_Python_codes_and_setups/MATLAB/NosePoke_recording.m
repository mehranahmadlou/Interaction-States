clear
mouse_folder = 'Z:\public\projects\MeAh_JuDz_20210211_Optogenetics_Behavior\Self_Stimulation\NewSetUp\1121973x';
session = daq.createSession('ni');
session.Rate=100;
% session.IsContinuous = true;
addAnalogInputChannel(session,'NIDAQ_run', [1,2] , 'Voltage');
session.DurationInSeconds = 3600; %3600; % 1 hr
prepare(session)
data = startForeground(session);
save([mouse_folder,'\nose_poke.mat'],'data')