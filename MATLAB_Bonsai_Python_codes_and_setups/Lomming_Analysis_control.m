k = 1121123;
Opto_order = 2;

[A,B,C] = xlsread(['data_path\',num2str(k),'\output\center.csv']);
[Shelter,~,~] = xlsread(['data_path\',num2str(k),'\output\shelter.csv']);
[A1,B1,C1] = xlsread(['data_path\',num2str(k),'\output\opto.csv']);
[Loom,~,~] = xlsread(['data_path\',num2str(k),'\loom0.csv']);
[key_press,~,~] = xlsread(['data_path\',num2str(k),'\tick_time_keypress0.csv']);
[movie_start,~,~] = xlsread(['data_path\',num2str(k),'\moviestart0.csv']);

% first few could be 'NAN' elements
AX = cellfun(@ischar,C,'UniformOutput',false);
AXX = cell2mat(AX);
ax = find(diff(AXX(:,1))==-1); 
if ~isempty(ax)
    A = [NaN(ax(1),2);A];
end

% interpolation to fill the missing points
Ax1 = A(:,1)';
X1 = ~isnan(Ax1);
Y1 = cumsum(X1-diff([1,X1])/2);
Z1 = interp1(1:nnz(X1),Ax1(X1),Y1);
Ax2 = A(:,2)';
X2 = ~isnan(Ax2);
Y2 = cumsum(X2-diff([1,X2])/2);
Z2 = interp1(1:nnz(X2),Ax2(X2),Y2);
A = 0.12*[Z1',Z2']; % 0.12 converting px to cm
XYdiff = [NaN,NaN;movmean(diff(A),25,'omitnan')];
% XYdiff = [NaN,NaN;diff(A)];
SpeedA = sqrt(XYdiff(:,1).^2+XYdiff(:,2).^2);
SpeedA = movmean(SpeedA,25,'omitnan');
% loom intensities
Loom_intensity = unique(Loom);

% Opto 

Opto = 0;
for i = 1:2:length(key_press)
    Opto(i) = 0;
end
for i = 2:2:length(key_press)
    Opto(i) = 1;
end
Opto = Opto';

% convert stimulus keypress to frame number from start of the movie
KPress = key_press-movie_start;
Key_Press_Frame = floor((KPress-300)/20.007);

% % if there is an opto output file use that instead of the keypress file 
% if ~isempty(A1)
%     S1 = A1>0.4;
%     [Key_Press_Frame,b] = find(diff(S1)==1);
% end



% in shelter
AS = movmean(Shelter,10);
amax = max(AS); amin = min(AS);
in_shelter = amax - 0.5*(amax-amin);
Shelter_In = AS < in_shelter;

% Speed before and after stimuli
SA = [];
ShIn = [];
for i = 1:length(key_press)
    SA = [SA,smooth(SpeedA(Key_Press_Frame(i)-250:Key_Press_Frame(i)+250),'sgolay')];
    ShIn = [ShIn,Shelter_In(Key_Press_Frame(i)-250:Key_Press_Frame(i)+250)];
end

% speed for each contrast
SA1 = SA(:,Loom == Loom_intensity(1)); % low contrast
SA2 = SA(:,Loom == Loom_intensity(2)); % medim contrast
SA3 = SA(:,Loom == Loom_intensity(3)); % high contrast

% in shelter for each contrast
ShIn1 = ShIn(:,Loom == Loom_intensity(1)); % low contrast
ShIn2 = ShIn(:,Loom == Loom_intensity(2)); % medim contrast
ShIn3 = ShIn(:,Loom == Loom_intensity(3)); % high contrast

imagesc(SA3(:,1:2:end)',[0,1]) % on heatmap
figure;imagesc(SA3(:,2:2:end)',[0,1]) % off heatmap

figure;imagesc(ShIn3(:,1:2:end)',[0,1]) % on heatmap
figure;imagesc(ShIn3(:,2:2:end)',[0,1]) % off heatmap

imagesc(SA2(:,1:2:end)',[0,1]) % on heatmap
figure;imagesc(SA2(:,2:2:end)',[0,1]) % off heatmap

figure;imagesc(ShIn2(:,1:2:end)',[0,1]) % on heatmap
figure;imagesc(ShIn2(:,2:2:end)',[0,1]) % off heatmap