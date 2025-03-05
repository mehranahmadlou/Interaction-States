load('Explore_Exploit_database.mat')
S = ExEx_database;

B6 = [];
V2ACR2 = [];
V2ChR2 = [];
V3ACR2 = [];
V3ChR2 = [];
VgatACR2 = [];
VgatChR2 = [];
SertACR2 = [];
SertChR2 = [];
LHbACR2 = [];
LHbChR2 = [];
IPNACR2 = [];
IPNChR2 = [];
MRNIPNACR2 = [];
VgatHACR2 = [];
VgatHChR2 = [];

for i=1:length(S)
    if strcmp(S(i).group,'Vglut2_MnR_stGtACR2')==1
        V2ACR2 = [V2ACR2,i];
    elseif strcmp(S(i).group,'Vglut2_MnR_ChR2')==1
        V2ChR2 = [V2ChR2,i];
    elseif strcmp(S(i).group,'Vglut3_MnR_stGtACR2')==1
        V3ACR2 = [V3ACR2,i];
    elseif strcmp(S(i).group,'Vglut3_MnR_ChR2')==1
        V3ChR2 = [V3ChR2,i];
    elseif strcmp(S(i).group,'VGAT_MnR_stGtACR2')==1
        VgatACR2 = [VgatACR2,i];
    elseif strcmp(S(i).group,'VGAT_MnR_ChR2')==1
        VgatChR2 = [VgatChR2,i];
    elseif strcmp(S(i).group,'SERT_MnR_stGtACR2')==1
        SertACR2 = [SertACR2,i];
    elseif strcmp(S(i).group,'SERT_MnR_ChR2')==1
        SertChR2 = [SertChR2,i];
    elseif strcmp(S(i).group,'Hypothal_VGAT_MRN_eNpHR3.0')==1
        VgatHACR2 = [VgatHACR2,i];
    elseif strcmp(S(i).group,'Hypothal_VGAT_MRN_ChR2')==1
        VgatHChR2 = [VgatHChR2,i];
    elseif strcmp(S(i).group,'LHb_MRN_eNpHR3.0')==1
        LHbACR2 = [LHbACR2,i];
    elseif strcmp(S(i).group,'LHb_MRN_ChR2')==1
        LHbChR2 = [LHbChR2,i];
    elseif strcmp(S(i).group,'VGAT_IPN_MRN_eNpHR3.0')==1
        IPNACR2 = [IPNACR2,i];
    elseif strcmp(S(i).group,'VGAT_IPN_MRN_ChR2')==1
        IPNChR2 = [IPNChR2,i];
    elseif strcmp(S(i).group,'VGAT_MRN_IPN_eNpHR3.0')==1
        MRNIPNACR2 = [MRNIPNACR2,i];

    elseif strcmp(S(i).group,'Control')==1
        %     if strcmp(S(i).group,'Hypothal_VGAT_MRN_ChR2')==1
        B6 = [B6,i];
    end
end

%% exponential fitting

Gr = {B6,V2ACR2,V2ChR2,V3ACR2,V3ChR2,VgatACR2,VgatChR2,SertACR2,SertChR2,VgatHACR2,VgatHChR2,LHbACR2,LHbChR2,IPNACR2,IPNChR2,MRNIPNACR2};
GrLable = {'B6','V2 ACR2','V2 ChR2','V3 ACR2','V3 ChR2','VGAT ACR2','VGAT ChR2','SERT ACR2','SERT ChR2','VgatLH NpHR','VgatLH ChR2','LHb NpHR','LHb ChR2','VgatIPN NpHR','VgatIPN ChR2','VgatMRN IPN NpHR'};
SL = {}
for i = 1:length(Gr)
    Sl = exp_fit_slope(ExEx_database,Gr{i});
    SL = [SL,abs(Sl)];
end

% ivt_graph({SL{1},SL{2},SL{3},SL{4},SL{5},SL{6},SL{7},SL{8},SL{9},SL{10},SL{11},SL{12},SL{13},SL{14},SL{15},SL{16}},[],'xticklabels',GrLable,'rotate_xticklabels',60,'fontsize',10,'showpoints',1,'style','box','errorbars','sem','test','none')


Gr = {B6,V2ACR2,V2ChR2,V3ACR2,V3ChR2,VgatACR2,VgatChR2,SertACR2,SertChR2,VgatHACR2,VgatHChR2,LHbACR2,LHbChR2,IPNACR2,IPNChR2,MRNIPNACR2};
Gr_Sw = {Sw_control,Sw_vglut2ACR2,Sw_vglut2ChR2,Sw_vglut3ACR2,Sw_vglut3ChR2,Sw_VgatACR2,Sw_VgatChR2,Sw_SertACR2,Sw_SertChR2,Sw_VgatHACR2,Sw_VgatHChR2,Sw_LHbACR2,Sw_LHbChR2,Sw_IPNACR2,Sw_IPNChR2,Sw_MRNIPNACR2};

GrLable = {'tdTom','V2 ACR2','V2 ChR2','V3 ACR2','V3 ChR2','VGAT ACR2','VGAT ChR2','SERT ACR2','SERT ChR2','VgatLH NpHR','VgatLH ChR2','LHb NpHR','LHb ChR2','VgatIPN NpHR','VgatIPN ChR2','VgatMRN IPN NpHR'};

Sw_Num = {}
for i = 1:length(Gr_Sw)
    Sw_Num = [Sw_Num,Gr_Sw{i}/10];
end

ivt_graph({SL{1},SL{2},SL{3},SL{4},SL{5},SL{6},SL{7},SL{8},SL{9}},[],'xticklabels',GrLable([1:9]),'rotate_xticklabels',60,'fontsize',10,'showpoints',1,'style','box','errorbars','sem','test','none')
% ,SL{10},SL{11},SL{12},SL{13},SL{14},SL{15},SL{16}
ivt_graph({Sw_Num{1},Sw_Num{2},Sw_Num{3},Sw_Num{4},Sw_Num{5},Sw_Num{6},Sw_Num{7},Sw_Num{8},Sw_Num{9}},[],'xticklabels',GrLable([1:9]),'rotate_xticklabels',60,'fontsize',10,'showpoints',1,'style','box','errorbars','sem','test','none')
% ,Sw_Num{10},Sw_Num{11},Sw_Num{12},Sw_Num{13},Sw_Num{14},Sw_Num{15},Sw_Num{16}

% xxx = 0:1/15:1; 
% rng(1); a1 = randperm(16); 
% rng(2); a2 = randperm(16);
% rng(3); a3 = randperm(16);
% col = [xxx(a1);xxx(a2);xxx(a3)]';


% col = [0 0 0;0.7 0.1 0.7;1 0 1;0.7 0.1 0.1;1 0 0;0.1 0.7 0.1;0 1 0;0.1 0.1 0.7;0 0 1];
color_sig = [0.32,0.32,0.32;0.75,0.96,0.68;0.47,0.67,0.19;0.62,0.83,0.92;0.00,0.45,0.74;0.90 0.72 0.12;0.70 0.42 0.00;0.89,0.32,0.32;0.59,0.12,0.12];

figure;
hold on;
kInd = [1 16];
kIndCol = [1 9]; ii=0;
for i = kInd %length(Gr_Sw)
    ii=ii+1;
    scatter(SL{i},Sw_Num{i},30,'MarkerFaceColor',color_sig(kIndCol(ii),:),'MarkerEdgeColor',color_sig(kIndCol(ii),:));legend(GrLable(kInd),'FontSize',12,'EdgeColor','None');
end

axis square
axis equal

xlim([-1 15])
ylim([-1 15])

ylabel('Switching (N/10)','FontSize',18)
xlabel('Homogeneity Index','FontSize',18)

box off
set(gcf,'color','white')
hold off



figure;
hold on;
kInd = [1 16];
kIndCol = [1 9]; ii=0;
for i = kInd %length(Gr_Sw)
    ii=ii+1;
    errorbar(mean(SL{i}),mean(Sw_Num{i}),sem(SL{i}),-sem(SL{i}),sem(Sw_Num{i}),-sem(Sw_Num{i}),'o','MarkerSize',10,'MarkerEdgeColor',color_sig(kIndCol(ii),:),'MarkerFaceColor',color_sig(kIndCol(ii),:),'Color',color_sig(kIndCol(ii),:));
    
end

legend(GrLable(kInd),'FontSize',12,'EdgeColor','None');

axis square
axis equal

xlim([-1 15])
ylim([-1 15])

ylabel('Switching (N/10)','FontSize',18)
xlabel('Homogeneity Index','FontSize',18)

box off
set(gcf,'color','white')
hold off


Gr_ExExDis = {[30 56 14],[40 47 13],[11 84 6],[18 73 8],[26 61 13],[99 0.5 0.5],[28 60 12],[5 65 30],[59 37 5],[9 69 22],[96 2 2],[23 51 26],[3 14 82],[16 63 21],[76 11 13],[51 41 8]};

figure;
hold on;
kInd = [1 2:9];
kIndCol = [1 2:9]; ii=0;
for i = kInd %length(Gr_Sw)
    ii=ii+1;
    plot3(Gr_ExExDis{i}(1),Gr_ExExDis{i}(2),Gr_ExExDis{i}(3),'o','MarkerSize',10,'MarkerEdgeColor',color_sig(kIndCol(ii),:),'MarkerFaceColor',color_sig(kIndCol(ii),:),'Color',color_sig(kIndCol(ii),:));
    
end

legend(GrLable(kInd),'FontSize',12,'EdgeColor','None');

xlim([0 100])
ylim([0 100])
zlim([0 100])

xlabel('Exploitation (%)','FontSize',18)
ylabel('Exploration (%)','FontSize',18)
zlabel('Disengagement (%)','FontSize',18)

box off
grid on
set(gcf,'color','white')
hold off


function Sl = exp_fit_slope(Xdata,A)

x = 0:19;
f = @(b,x) b(1).*exp(b(2).*x)+b(3);

OD = [];
for x = A %V3ACR2 %VgatACR2 %B6 %V2ACR2
    for k = 1:length(Xdata(x).data)
        E = Xdata(x).data{1, k} ;
        AA = fieldnames(E);
        ObjStarts = []; % number of interactions per object
        ObjDur = []; % duration of interactions per object
        for  i = 7:2:46
            ObjStarts = [ObjStarts;length(E.(AA{i}))];
            ObjDur = [ObjDur;sum(E.(AA{i+1})-E.(AA{i}))];
        end
        %         hold on; bar(sort(ObjDur,'descend'),'r')
        OD = [OD,sort(ObjDur,'descend')];
        %         OD = [OD,sort(ObjStarts,'descend')];
    end
end
figure;
hold on
bar(mean(OD')./max(mean(OD')),'r')
set(gcf,'color','white')
box off
title('xxx','FontSize',20) %'Vglut2 ChR2'
ylabel('Duration of Interactions','FontSize',16)
% ylabel('Number of Interactions','FontSize',16)
xlabel('Sorted Object #','FontSize',16)
ylim([0 1.1])

Sl = [];
for i = 1:size(OD,2)
    y = OD(:,i)/max(OD(:,i));
    B = fminsearch(@(b) norm(y - f(b,x)), [-0.5; 0.5; 0.05]); Sl = [Sl,B(2)];
end

end