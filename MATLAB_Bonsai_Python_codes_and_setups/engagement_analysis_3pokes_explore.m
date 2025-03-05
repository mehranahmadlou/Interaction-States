% task names
TaskName = {'poke_noise_reward_optogenetics','poke_noise_reward_optogenetics2min',...
    'poke_noise_reward_optogenetics_3pokes','poke_noise_reward_optogenetics_autotrigger_0Hz_reengagement'};

% DP_Control = {'data_paths'};


DP_VGAT_ChR2 = {'data_paths'}; DP = DP_VGAT_ChR2;

for ti = 1:length(DP)
datapath = DP{ti};

% datapath = DP{1};

kk = dir(fullfile([datapath,'\'],'*.txt*'));
filename = kk.name;

str = fileread([datapath,'\',filename]);
TextAsCells = regexp(str, '\n', 'split');
for k = 1:length(TaskName)
    if strcmp(TextAsCells{1,2}(15:end),TaskName{k})
        Task = TaskName{k};
    end
end

S = TextAsCells{1,8}(4:end-1); St = convertCharsToStrings(S); st = split(St,","); 
for k = 1:length(st), States(1:2,k) = split(st(k),": "); end
state_labels = str2double(States(2,:));

E = TextAsCells{1,10}(4:end-1); Ev = convertCharsToStrings(E); ev = split(Ev,",");
for k = 1:length(ev), Events(1:2,k) = split(ev(k),": "); end
event_labels = str2double(Events(2,:));

first_D = 0;
i = 0;

while first_D == 0
    i = i+1;
    if ~isempty(TextAsCells{1,i})
        first_D = strcmp(TextAsCells{1,i}(1:2), 'D ');
    end
end

% Data = TextAsCells of D1 to Dend
D1 = i;
Dend = length(TextAsCells) - 1;

data = []; 
for i = D1:Dend
    if strcmp(TextAsCells{1,i}(1:2), 'D ')
        D = split(TextAsCells{1,i}); data = [data;[str2num(D{2}),str2num(D{3})]]; 
    end
end

% figure;plot(data(data(:,2)>3,1)/1000,data(data(:,2)>3,2),'o'); xlim([0 1800])
% figure;plot(data(data(:,2)<4,1)/1000,data(data(:,2)<4,2),'o'); xlim([0 1800])

%% states patch plot
s1_time = data(data(:,2)==1,1); % if length(s2_time)<length(s1_time), s1_time = s1_time(1:end-1); end;
s2_time = data(data(:,2)==2,1);
s3_time = data(data(:,2)==3,1);


%% events patch plot
e6_time = data(data(:,2)==6,1); % lick_detect   > distraction in a certain condition
e4_time = data(data(:,2)==4,1); % poke (port 1)
e9_time = data(data(:,2)==9,1); % opto_on
[e9_order,~] = find(data(:,2)==9);
e11_time = data(data(:,2)==11,1); % poke 2   > distraction
e13_time = data(data(:,2)==13,1); % poke 3   > distraction


% how long after opto completes one trial
B = [];
for i = 1:length(e9_time)-1
    if (e9_time(i+1) - e9_time(i) > 3000) && (e9_time(i) < 1200000)
        b = s3_time - e9_time(i); x = min(b(b > 0));
        [xx,~] = find(data(:,1) == s3_time((s3_time == (e9_time(i) + x))));
        Xd = data(e9_order(i):xx-1,2);
        B = [B , sum(Xd==11) + sum(Xd==13) + sum(Xd==6)];
%         B = [B , sum(Xd==11) + sum(Xd==13)];
    end
end


save([datapath,'\opto_3poke_explore.mat'],'B')
end