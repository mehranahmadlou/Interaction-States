% task names
TaskName = {'poke_noise_reward_optogenetics','poke_noise_reward_optogenetics2min',...
    'poke_noise_reward_optogenetics_3pokes','poke_noise_reward_optogenetics_autotrigger_0Hz_reengagement'};

DP = {'data_path'};

for ti = 1

datapath = DP{ti};

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

figure;plot(data(data(:,2)>3,1)/1000,data(data(:,2)>3,2),'o'); xlim([0 1800])
figure;plot(data(data(:,2)<4,1)/1000,data(data(:,2)<4,2),'o'); xlim([0 1800])

%% states patch plot
s1_time = data(data(:,2)==1,1)/1000; % if length(s2_time)<length(s1_time), s1_time = s1_time(1:end-1); end;
s2_time = data(data(:,2)==2,1)/1000;
s3_time = data(data(:,2)==3,1)/1000;
figure; subplot(2,1,1); hold on;
for j = 1:length(s1_time)-1
x = [s1_time(j) s2_time(j)-0.001 s2_time(j)-0.001 s1_time(j)];
y = [0 0 1 1];
p = patch(x,y,'blue')
p.EdgeColor = [0 0 1];
end
for j = 1:length(s2_time)-1
x = [s2_time(j) s3_time(j)-0.001 s3_time(j)-0.001 s2_time(j)];
y = [1 1 2 2];
p = patch(x,y,'red')
p.EdgeColor = [1 0 0];
end
for j = 1:length(s3_time)-1
x = [s3_time(j) s1_time(j+1)-0.001 s1_time(j+1)-0.001 s3_time(j)];
y = [2 2 3 3];
p = patch(x,y,'green')
p.EdgeColor = [0 1 0];
end

%% events patch plot
e6_time = data(data(:,2)==6,1)/1000;
e4_time = data(data(:,2)==4,1)/1000;
e9_time = data(data(:,2)==9,1)/1000;
subplot(2,1,2); hold on;
for j = 1:length(e4_time)
x = [e4_time(j) e4_time(j)+0.001 e4_time(j)+0.001 e4_time(j)];
y = [0 0 1 1];
p = patch(x,y,'red')
p.EdgeColor = [1 0 0];
end
for j = 1:length(e6_time)
x = [e6_time(j) e6_time(j)+0.001 e6_time(j)+0.001 e6_time(j)];
y = [1 1 2 2];
p = patch(x,y,'blue')
p.EdgeColor = [0 0 1];
end
for j = 1:length(s3_time)-1
x = [s3_time(j) s3_time(j)+0.001 s3_time(j)+0.001 s3_time(j)];
y = [2 2 3 3];
p = patch(x,y,'green')
p.EdgeColor = [0 1 0];
end
for j = 1:length(e9_time)
x = [e9_time(j) e9_time(j)+0.001 e9_time(j)+0.001 e9_time(j)];
y = [3 3 4 4];
p = patch(x,y,'blue')
p.EdgeColor = [0 0 1];
end
set(gcf,'renderer','Painters')
% how long after opto pokes
A = [];
for i = 1:length(e9_time)-1
    if e9_time(i+1) - e9_time(i) > 3
    a = s2_time-e9_time(i); A = [A,min(a(a > 0))];
    end
end
% figure;x=histogram(A,'BinWidth',0.5,'FaceColor',[0 0 1],'FaceAlpha',0.3)

% how long after opto completes one trial
B = [];
for i = 1:length(e9_time)-1
    if e9_time(i+1) - e9_time(i) > 3
    b = s3_time-e9_time(i); B = [B,min(b(b > 0))];
    end
end
% hold on;y=histogram(B,'BinWidth',0.5,'FaceColor',[0 1 0],'FaceAlpha',0.3)

% save([datapath,'\opto_poke_histograms.mat'],'x','y')
end