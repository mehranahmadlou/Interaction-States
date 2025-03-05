filepath = 'data_path';
F = {'Opto','BeforeOpto','AfterOpto'};

if isfile([filepath,'TOP.txt'])
    a = 'TOP';
elseif isfile([filepath,'BOTTOM.txt'])
    a = 'BOTTOM';
end

for k =1:3
cd([filepath,F{k}]);
A = VideoReader('crop.avi');  %% reading the crop movie
A1 = read(A,50);
imshow(A1);
ROI_rect = imrect(gca,[]);
% wait(ROI_rect);
Rect1 = floor(getPosition(ROI_rect));
A2 = A1(Rect1(2):Rect1(2)+Rect1(4),Rect1(1):Rect1(1)+Rect1(3),3);   % ROI number 1
close;
imshow(A2);pause(1);close
imshow(A1);
ROI_rect = imrect(gca,[]);
% wait(ROI_rect);
Rect2 = floor(getPosition(ROI_rect));
A3 = A1(Rect2(2):Rect2(2)+Rect2(4),Rect2(1):Rect2(1)+Rect2(3),3);  % ROI number 2
close;
imshow(A3);pause(1);close
[X1,X2,X3] = xlsread('center.csv');
nnn = split(X2,[' '])
X = str2double(nnn);
 % reading the centroid file
Y = [X(~isnan(X(:,1)),1) X(~isnan(X(:,2)),2)]; % removing NaN
ROI1 = [];
ROI2 = [];
for i = 1:length(Y)
    if (Y(i,2) > Rect2(2)) && (Y(i,2) < Rect2(2)+Rect2(4)) && (Y(i,1) > Rect2(1)) && (Y(i,1) < Rect2(1)+Rect2(3))
        ROI2 = [ROI2,i];
    elseif (Y(i,2) > Rect1(2)) && (Y(i,2) < Rect1(2)+Rect1(4)) && (Y(i,1) > Rect1(1)) && (Y(i,1) < Rect1(1)+Rect1(3))
        ROI1 = [ROI1,i];
%     elseif (Y(i,2) > Rect2(2)) && (Y(i,2) < Rect2(2)+Rect2(4)) && (Y(i,1) > Rect2(1)) && (Y(i,1) < Rect2(1)+Rect2(3))
%         ROI2 = [ROI2,i];
    end
end
figure;plot(ROI1,ones(1,length(ROI1)),'bo')
hold on;plot(ROI2,ones(1,length(ROI2)),'ro')
roi_left = ROI1; %top
roi_right = ROI2; %bottom
save('double_chamber_result.mat','roi_left','roi_right','a')
pause(2)
close all
end