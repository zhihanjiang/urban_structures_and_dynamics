clc;close all;
load('NDS');

i =[50,51,49,49];
j =[57,57,28,27];
M = 1;
Ncoord = [i;j];
Ngrids = zeros(4,24*7);

for N =1:4
    x = Ncoord(M,N);
    y = Ncoord(M+1,N);
    c = squeeze(NDS(x,y,:));
    c = c';
    sum1 = [];
    for n = 1:2:1439
        sum1 = [sum1 c(1,n)+c(1,n+1)];
    end
    sum2 = sum1(:,4*24+1:4*24+24*7*3);
    sum2 = mean(reshape(sum2',24*7,3),2);
    m = sum2';
    Ngrids(N,:)=m;
end
NGrids = Ngrids';
csvwrite('NGrids.csv',NGrids);



% g = NGrids(3,:);%randi（Nm）表示1到Nm中的任意一个数
% clc; close all; 
% figure('Position',[500,500,400,200]);%图像窗口的位置及其大小，500,500表示起始坐标，400表示宽，200表示长
% plot(g,'g','LineWidth',2);
% xlim([1,168]);
% axis tight;
% ax = gca;
% ax.XTick = 1:24:168; 
% ax.XTickLabel = {'MON','TUE','WED','THU','FRI','SAT','SUN'};
% grid on; 
% set(gca,'FontSize', 15);

