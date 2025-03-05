function E = AppendE(E)

AA = fieldnames(E);

ObjStarts = []; % number of interactions per object
ObjDur = []; % duration of interactions per object
for  i = 7:2:46
    ObjStarts = [ObjStarts;length(E.(AA{i}))];
    ObjDur = [ObjDur;sum(E.(AA{i+1})-E.(AA{i}))];
end

ObjSniff = 0;
for t=1:length(E.AppSniff_start)
for i=7:2:46
    for  k = 1:length(E.(AA{i}))
        if abs(E.AppSniff_start(t)-E.(AA{i})(k))<0.1 && abs(E.AppSniff_end(t)-E.(AA{i+1})(k))<0.1
%             i
            objind = floor((i-6)/2)+1;
            ObjSniff(t) = objind;
        end
    end
end
end

E.objSniff = ObjSniff;

ObjDeep = 0;
for t=1:length(E.DeepInteract_start)
for i=7:2:46
    for  k = 1:length(E.(AA{i}))
        if abs(E.DeepInteract_start(t)-E.(AA{i})(k))<0.1 && abs(E.DeepInteract_end(t)-E.(AA{i+1})(k))<0.1
%             i
            objind = floor((i-6)/2)+1;
            ObjDeep(t) = objind;
        end
    end
end
end

E.objDeep = ObjDeep;

