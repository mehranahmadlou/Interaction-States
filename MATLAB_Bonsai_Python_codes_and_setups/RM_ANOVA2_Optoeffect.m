% VGAT

Y_opto = Ch3(:);
S_opto = (repmat(1:6,[1,10]))';
Y_noopto = K3(:);
S_noopto = (repmat(1:6,[1,10]))';
Y = [Y_opto;Y_noopto];
S = [S_opto;S_noopto];
F1 = [ones(60,1);2*ones(60,1)]; % opto factor
Torder = repmat(1:10,[6,1]);
F2 = [Torder(:);Torder(:)]; % trial order factor
FactNames = {'Opto', 'Tr_order'};
stats = rm_anova2(Y,S,F1,F2,FactNames)

% VGLUT2

Y_opto = Ch3(:);
S_opto = (repmat(1:11,[1,4]))';
Y_noopto = KK3(:);
S_noopto = (repmat(1:11,[1,4]))';
Y = [Y_opto;Y_noopto];
S = [S_opto;S_noopto];
F1 = [ones(44,1);2*ones(44,1)]; % opto factor
Torder = repmat(1:4,[11,1]);
F2 = [Torder(:);Torder(:)]; % trial order factor
FactNames = {'Opto', 'Tr_order'};
stats = rm_anova2(Y,S,F1,F2,FactNames)

