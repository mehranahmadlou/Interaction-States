%% double chamber database
% dd = dir(fullfile(['Y:\mrsic_flogel\public\projects\MeAh_JuDz_20210211_Optogenetics_Behavior\double_chamber','\*2021*']));
% for i=1:length(dd)
%     doublechamber_db(i).name = dd(i).name(1:7);
%     doublechamber_db(i).path = fullfile([dd(i).folder,'\',dd(i).name]);
% end

%% double chamber data
load 'Y:\mrsic_flogel\public\projects\MeAh_JuDz_20210211_Optogenetics_Behavior\double_chamber\doublechamber_database.mat'

for i = 1:length(doublechamber_db)
    d = dir(fullfile([doublechamber_db(i).path,'\*\','double_chamber_result.mat']));
    if isempty(d)==0
       Opto = load([doublechamber_db(i).path,'\Opto\','double_chamber_result.mat']);
       doublechamber_db(i).Opto = [length(Opto.roi_left),length(Opto.roi_right)];
       BeforeOpto = load([doublechamber_db(i).path,'\BeforeOpto\','double_chamber_result.mat']);
       doublechamber_db(i).BeforeOpto = [length(BeforeOpto.roi_left),length(BeforeOpto.roi_right)];
       AfterOpto = load([doublechamber_db(i).path,'\AfterOpto\','double_chamber_result.mat']);
       doublechamber_db(i).AfterOpto = [length(AfterOpto.roi_left),length(AfterOpto.roi_right)];
    end
end

%% double chamber groupmate
vgatMRN_ACR2 = [];
for i = 1:length(doublechamber_db)
    if strcmp(doublechamber_db(i).group,'vgatMRN_ACR2')==1
        vgatMRN_ACR2 = [vgatMRN_ACR2,i];
    end
end

BO=[];O=[];
for i = vgatMRN_ACR2
    BO = [BO,doublechamber_db(i).BeforeOpto(1)/sum(doublechamber_db(i).BeforeOpto(:))];
    O = [O,doublechamber_db(i).Opto(1)/sum(doublechamber_db(i).Opto(:))];
end
BO_vgat = BO; O_vgat = O;

BO=[];O=[];
for i = vgatMRN_ACR2
    BO = [BO,doublechamber_db(i).BeforeOpto(1)/sum(doublechamber_db(i).BeforeOpto(:))];
    O = [O,doublechamber_db(i).Opto(1)/sum(doublechamber_db(i).Opto(:))];
end
BO_cont = BO; O_cont = O;
%% plot some stuff
% 
% B = {[8426,5816];[4625,9852];[2189,12577];[6515,7912];[4604,9150];[6522,7886];[10984,3511];[9775,3826];[10047,3939];[6248,8324];[7040,6455];[8217,6478];[8447,5277];[11498,2922];[11381,3096];[11524,2681]};
% C = cell2mat(B)
% 100*(C(:,1)-C(:,2))./(C(:,1)+C(:,2))
% LHBMRN = [18.3261, -36.1055]; Vglut2 = -70.3508; cont = [-9.6832, -9.4670]; mPFCChR2 = -33.0522; VgatHyp = 51.5557; VgatACR2 = [43.7394 , 43.6722]; mPFCACR2 = [-14.2465, 4.3349]; SERT = [11.8340 , 23.0982]; Vglut3 = [59.4730 , 57.2287 , 62.2527];
% ivt_graph({cont,LHBMRN,Vglut2,mPFCChR2,VgatHyp,VgatACR2,mPFCACR2,SERT,Vglut3},[],'xticklabels',{'cont','LHBMRN','Vglut2','mPFCChR2','VgatHyp','VgatACR2','mPFCACR2','SERT','Vglut3'},'showpoints',1,'style','box','errorbars','sem')
