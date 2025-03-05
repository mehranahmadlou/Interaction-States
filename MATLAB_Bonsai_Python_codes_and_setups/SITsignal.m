folder_data = 'Z:\mrsic_flogel\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Explore_Exploit_Objects\JAABA_ANALYSIS\OFF\';
dd = dir(fullfile([folder_data,'\**\'],'*Cent_mouse.mat'));

for k = 1:length(dd)
    sit_signal = zeros(1,6001);
    track_path = dd(k).folder;
    load([movie_path,'\Cent_mouse.mat']);
    x5=diff(Cent_mouse);
    d5=sqrt(x5(:,1).^2+x5(:,2).^2);
    c5 = sgolayfilt(d5,3,11);
    sit_time = c5<2;
    x1 = diff(sit_time);
    y1 = find(x1==1);
    y2 = find(x1==-1);
    if length(y2)<length(y1)
        y2 = [y2;6001];
    end
    xy = y2-y1;
    sxy = find(xy>20);
    for i=1:length(sxy)
        sit_signal(y1(sxy(i))+1:y2(sxy(i)))=1;
    end
        save([track_path,'\sit_signal.mat'],'sit_signal')
end

% %% sniffing the same object or a different one
% x = diff([0 E.objSniff]);
% x(x~=0)=1;

