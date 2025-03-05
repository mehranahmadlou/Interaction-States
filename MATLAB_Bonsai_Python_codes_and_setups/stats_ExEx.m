
cd Z:\mrsic_flogel\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Explore_Exploit_Objects\JAABA_ANALYSIS\EXEx\

%% STATS with BonF correction SERT
load ExEx_C.mat
load ExEx_SERT_Inh.mat
load ExEx_SERT_Ex.mat
%Exploit
ExEx = {Exploit_C , Exploit_SERT_Ex, Exploit_SERT_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Explore
ExEx = {Explore_C , Explore_SERT_Ex, Explore_SERT_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Disengage
ExEx = {Disengage_C , Disengage_SERT_Ex, Disengage_SERT_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)

%% STATS with BonF correction VGAT
load ExEx_VGAT_Inh.mat
load ExEx_VGAT_Ex.mat
%Exploit
ExEx = {Exploit_C , Exploit_VGAT_Ex, Exploit_VGAT_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Explore
ExEx = {Explore_C , Explore_VGAT_Ex, Explore_VGAT_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Disengage
ExEx = {Disengage_C , Disengage_VGAT_Ex, Disengage_VGAT_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)

%% STATS with BonF correction VGluT2
load ExEx_VGluT2_Inh.mat
load ExEx_VGluT2_Ex.mat
%Exploit
ExEx = {Exploit_C , Exploit_VGluT2_Ex, Exploit_VGluT2_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Explore
ExEx = {Explore_C , Explore_VGluT2_Ex, Explore_VGluT2_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Disengage
ExEx = {Disengage_C , Disengage_VGluT2_Ex, Disengage_VGluT2_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)

%% STATS with BonF correction LHb
load ExEx_LHb_Inh.mat
load ExEx_LHb_Ex.mat
%Exploit
ExEx = {Exploit_C , Exploit_LHb_Ex, Exploit_LHb_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Explore
ExEx = {Explore_C , Explore_LHb_Ex, Explore_LHb_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Disengage
ExEx = {Disengage_C , Disengage_LHb_Ex, Disengage_LHb_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)

%% STATS with BonF correction LHA
load ExEx_LHA_Inh.mat
load ExEx_LHA_Ex.mat
%Exploit
ExEx = {Exploit_C , Exploit_LHA_Ex, Exploit_LHA_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Explore
ExEx = {Explore_C , Explore_LHA_Ex, Explore_LHA_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Disengage
ExEx = {Disengage_C , Disengage_LHA_Ex, Disengage_LHA_Inh};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2 3]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[2*p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)

%% STATS with BonF correction LHA VGLU2
load ExEx_V2LHA_Exc.mat
%Exploit
ExEx = {Exploit_C , Exploit_V2LHA_Exc};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Explore
ExEx = {Explore_C , Explore_V2LHA_Exc};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)
%Disengage
ExEx = {Disengage_C , Disengage_V2LHA_Exc};
i=1; [mean(ExEx{i}),sem(ExEx{i})]
P = [];
M = [];
for  i = [2]
    [~,p,~,stats] = ttest2(ExEx{1},ExEx{i}); P = [P;[p stats.tstat stats.df]];
    M = [M;[mean(ExEx{i}),sem(ExEx{i})]];
end
display(P)
display(M)