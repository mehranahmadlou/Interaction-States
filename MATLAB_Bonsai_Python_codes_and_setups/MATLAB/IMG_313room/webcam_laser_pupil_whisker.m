w = webcamlist;  % 'DMK 23UV024'
cam_pupil = webcam(w{1}); % 'DMK 22BUC03' ; fps:30 ; Resolution:744x480
cam_whisker = webcam(w{2});  % 'DMK 23UV024'
vidWriter_pupil = VideoWriter('pupil.avi');
open(vidWriter_pupil);
vidWriter_whisker = VideoWriter('whisker.avi');
open(vidWriter_whisker);
tic
for index = 1:60
    % Acquire frame for processing
    img1 = snapshot(cam_pupil);
    img2 = snapshot(cam_whisker);
    imshow(1-im2bw(img1,0.25))
%     imshow(img)
    % Write frame to video
    writeVideo(vidWriter_pupil, img1);
    writeVideo(vidWriter_whisker, img2);
end
toc
close(vidWriter_pupil);
close(vidWriter_whisker);
clear cam_pupil
clear cam_whisker