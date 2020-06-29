clear all;
load('AGP');
load('NPS');
sm = length(find(NPS>=300));%一天10辆，30天300辆的筛选粒度
mid = find(NPS>=300);
idx = kmeans(AGP,5,'rep',10);
lables = idx';
L = zeros(77,68);
L(mid)=lables;
save('L',L)
imagesc(L)
grid on