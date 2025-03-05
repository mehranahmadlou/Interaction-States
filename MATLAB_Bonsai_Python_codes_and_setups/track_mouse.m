folder_data = 'Z:\public\projects\MeAhetal_20210211_Optogenetics_Behavior\Explore_Exploit_Objects\JAABA_ANALYSIS\OFF\';
dd = dir(fullfile([folder_data,'\**\'],'*movie.avi'));

for k = 1:length(dd)
    
    movie_path = dd(k).folder;
    display(['file(',num2str(k),'): ',movie_path])
    xxx = VideoReader([movie_path,'\movie.avi']);
    
    a2 = 0;
    Cent_mouse = [];
    
    figure;hold on
    for i = 1:xxx.NumFrames
        frame1 = read(xxx,i);
        I = imcrop(frame1,[50, 0, 960, 1028]);
        x = im2bw(I,0.04); x = not(x);
        Ilabel = bwlabel(x,8);
        %     CC = bwconncomp(x,8);
        stat = regionprops(Ilabel,'centroid');
        stat2 = regionprops(Ilabel,'Area');
        [~,a2] = max([stat2.Area]);
        Cent_mouse = [Cent_mouse;stat(a2).Centroid];
        if mod(i,100) == 0
            pause(0.1)
            plot(Cent_mouse(i-99:i,1),Cent_mouse(i-99:i,2),'-o')
        end
    end
    close all
    save([movie_path,'\Cent_mouse.mat'],'Cent_mouse')
end







