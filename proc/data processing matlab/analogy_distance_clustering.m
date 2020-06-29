%% load data
clc; clear; close all;
% load('SMS_IN'); load('SMS_OUT'); load('SMS');
% load('CALL_IN'); 
% load('CALL_OUT'); 
% load('CALL');
% load('INTERNET');
% load('S');
load('PS');
load('DS');

sm = length(find(PS>=3600));
[i,j] = find(PS>=3600);
M = 1;
coord = [i';j'];
grids = zeros(sm,24*7);

for N =1:sm
    x = coord(M,N);
    y = coord(M+1,N);
    c = squeeze(DS(x,y,:));
    c = c';
    sum1 = [];
    for n = 1:2:1439
        sum1 = [sum1 c(1,n)+c(1,n+1)];
    end
    sum2 = sum1(:,4*24+1:4*24+24*7*3);
    sum2 = mean(reshape(sum2',24*7,3),2);
    m = sum2';
    grids(N,:)=m;
end
Grids = grids(:,1:24*7);
imagesc(Grids)

% Ng = 10000; Nt = 6*24*62; Nh = Nt/6;%Ng表示100*100个格子，Nh表示两个月共有多少小时
% Nm = sum(S);%对矩阵S的每列求和。Nm表示有182个基站。S为行向量


%% select Milano metropolitan areas
mid = find(PS>=3600);%找到矩阵S中非0元素的位置，mid为列向量
% M = INTERNET(mid,:);


%%
% clc;close all;
% m1 = M(999,:); m2 = M(1000,:); m3 = M(1001,:);
% mfigure();
% subplot(3,1,1);     plot(m1);
% subplot(3,1,2);     plot(m2);
% subplot(3,1,3);     plot(m3);


%% aggregate by hour and extract 8 good weeks
% H = squeeze(sum(reshape(M,Nm,6,Nh),2));%sum(A,2)代表求每行的和。6？？？
% H = H(:,24*3+1:24*3+24*7*8);%H为Nm*（24*8周）


%% training data: first 4 weeks, as a typical week
% W = H(:,1:24*7*4);         % W为Nm*（24*7*4 ）
% W = mean(reshape(W,Nm,24*7,4),3);%W为Nm*（24*7），每一个格子的数值代表4周对应时间的均值
% imagesc(W);


%% random grid traffic pattern
clc;close all;
g = Grids(randi(sm),:);%randi（Nm）表示1到Nm中的任意一个数
clc; close all; figure('Position',[500,500,400,200]);%图像窗口的位置及其大小，500,500表示起始坐标，400表示宽，200表示长
plot(g,'g','LineWidth',2);
xlim([1,168]); axis tight;
ax = gca; ax.XTick = 1:24:168; 
ax.XTickLabel = {'MON','TUE','WED','THU','FRI','SAT','SUN'};
grid on; set(gca,'FontSize', 15);


%% prepare distance matrix
Ng = 154*136;
[X,Y] = ind2sub([154,136],1:Ng);%将100*100的矩阵中的每个元素的索引转变为坐标，I表示行，J表示列.I、J均为行向量
GEODIST = squareform(pdist([Y',X']));
GEODIST = GEODIST(mid,mid);%GEODIST为Nm*Nm的距离矩阵
imagesc(GEODIST);


%% prepare similarity matrix
SIMDIST = (1 + corr(Grids'))/2;
SIMDIST(GEODIST==0) = 0;        %SIMDIST为Nm*Nm的相关系数矩阵，且对角线元素为0， remove self-loop
imagesc(SIMDIST); colorbar();


%% GCLP algorithm
clc;tic;
Nl = 10; Nc = 4;
DTHRES = sqrt(2*Nc*Nc);           % 1km range
C = randperm(sm);               % C为1到Nm的Nm个随机数字，为行向量。random initialization of labels
for lc = 1:Nl
    C0 = C;%？？？
    L = randperm(sm);%L为1到Nm的随机的Nm个数，例如：1,4,3,7,9，Nm.....2.L为行向量
    for i = 1:sm
        n = L(i);
        [a,~,c] = unique(C);%a为C中不重复的元素（有小到大排列），c表示C中元素在c中的位置
        dmax = accumarray(c,GEODIST(n,:),[],@max);%dmax和c一样是列向量。GEODIST(n,:)为行向量，每一个元素按c中元素的值重新排位置。
        aff = accumarray(c,SIMDIST(n,:));
        gain = aff.*log(DTHRES./dmax);
        [v,k] = max(gain);%返回行向量[v,k]。v为行向量，每一个元素代表gain中每列元素的最大值。k为行向量，每一个元素代表每列最大元素所在的行数。
%         [v,k] = max(aff);
        C(n) = a(k);
    end
    disp([num2str(lc),': ',num2str(length(aff))]);%num2str(lc)将1c中的数字转化为字符串，转化后可用fprintf或者disp函数进行输出。
    if C0 == C 
        break
    end
end
toc;
save('C','C');


%% display clusters
load('C');
F = zeros(154,136);
F(mid) = C;%将C中的元素一次放入mid值的位置处。例如：mid=45、48、50，C =[1,3,2],就把C中的1放入G中的45位，3放到48位，2放到50位
%F = rot90(F);%将G矩阵逆时针旋转90度
clc; close all; figure('Position',[500,500,500,500]);
imagesc(F);
axis off;


%% test grid and cluster traffic
% clc; close all;
% mfigure();
% % grid 5738: san siro
% h = H(mid==5738,:);
% subplot(2,1,1);
% plot(h);
% ax = gca; ax.XTick = 1:24*7:24*7*8; ax.XTickLabel = 1:7*8;
% xlabel('day'); ylabel('traffic');
% grid on; axis tight; set(gca,'FontSize', 17);
% % 1962: san siro
% h = sum(H(C==1962,:));
% subplot(2,1,2);
% plot(h);
% ax = gca; ax.XTick = 1:24*7:24*7*8; ax.XTickLabel = 1:7*8;
% xlabel('week'); ylabel('traffic'); 
% grid on; axis tight; set(gca,'FontSize', 20);
% ylim([0,3e4]);
% 
% 
% %% 2105: duomo
% clc; close all;
% h = sum(H(C==2105,1:24*7*4));
% h = reshape(h,24,7*4);
% figure('Position',[100,500,600,400]);
% imagesc(h); colorbar();
% ax = gca; ax.XTick = 1:7:7*4; ax.XTickLabel = 1:4;
% % ax = gca; ax.YTick = 1:2:24;
% xlabel('week'); ylabel('hour'); set(gca,'FontSize', 22);