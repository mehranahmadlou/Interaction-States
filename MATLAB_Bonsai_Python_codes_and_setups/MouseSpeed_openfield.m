% TRAVELED DISTANCE & SPEED in openfield

% datapaths for groups 
C{1} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\Cont\openfield\Tracks'; %Control
C{2} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\SERT\openfield\Tracks'; %SERT_Inh
C{3} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\VGAT\openfield\Tracks'; %VGAT_Inh
C{4} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\VGLUT2\openfield\Tracks'; %VGLUT2_Exc

% C{1} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\Cont\openfield\no_opto'; %Control
% C{2} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\SERT\openfield\no_opto'; %SERT_Inh
% C{3} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\VGAT\openfield\no_opto'; %VGAT_Inh
% C{4} = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Short_Opto_Object_Nature\VGLUT2\openfield\no_opto'; %VGLUT2_Exc

Velocity = {};
Vel_time = {};
for i = 1:length(C)

    path_data = dir([C{i},'\*.csv']);

    V_opto = [];
    Vt = [];
    for k = 1:length(path_data)

        % read mouse positions
        X2 = xlsread([C{i},'\',path_data(k).name]);

        % average speed
        dV = diff(X2);
        V_opto(k) = sum(sqrt(dV(:,1).^2+dV(:,2).^2))/length(dV);
        vc = sqrt(dV(:,1).^2+dV(:,2).^2)/9;
        Vt = [Vt,[vc;zeros(1500-length(vc),1)]];
    end
    Velocity{i} = 25*V_opto/18; % frame rate: 25 fps; resolution: 720 pixels per 40 cm (18 pixels/cm)
    Vel_time{i} = 25*Vt/18;
end


ivt_graph({Velocity{1},Velocity{2},Velocity{3},Velocity{4}},[],'xticklabels',{'Ctrl','SERT_Inh','VGAT_Inh','VGLUT2_Exc'},'showpoints',1,'errorbars','sem')

%% HISTOGRAMS

GrLable = {'Ctrl','V2 ACR2','V2 ChR2','VGAT ACR2','VGAT ChR2','SERT ACR2','SERT ChR2'};
color_sig = [0.32,0.32,0.32;0.75,0.96,0.68;0.47,0.67,0.19;0.62,0.83,0.92;0.00,0.45,0.74;0.90 0.72 0.12;0.70 0.42 0.00;0.89,0.32,0.32;0.59,0.12,0.12];

figure;subplot(2,2,1);bar(1:1500,mean(Vel_time{1, 1} ,2),1,'FaceColor',color_sig(1,:),'EdgeColor','none');
box off
set(gcf,'color','white')
set(gcf,'renderer','Painters')
ylim([0 5])
% title(GrLable{1})
subplot(2,2,2);bar(1:1500,mean(Vel_time{1, 3} ,2),1,'FaceColor',color_sig(4,:),'EdgeColor','none')
box off
set(gcf,'color','white')
set(gcf,'renderer','Painters')
ylim([0 5])
% title(GrLable{4})
subplot(2,2,3);bar(1:1500,mean(Vel_time{1, 2} ,2),1,'FaceColor',color_sig(6,:),'EdgeColor','none');
box off
set(gcf,'color','white')
set(gcf,'renderer','Painters')
ylim([0 5])
% title(GrLable{6})
subplot(2,2,4);bar(1:1500,mean(Vel_time{1, 4} ,2),1,'FaceColor',color_sig(3,:),'EdgeColor','none')
box off
set(gcf,'color','white')
set(gcf,'renderer','Painters')
ylim([0 5])
% title(GrLable{3})