clc;clear;close all;
% boundaries: degree * 1e6
T = 24561485;
B = 24423250;
R = 118198504;
L = 118064743;
tb = T - B;
rl = R - L;
% distances: meter
GRID = 100;
WE = 13550;
NS = 15388;
% times: in minutes
DURATION = 30;
START_TIME = datetime('09/01/2016 00:00','TimeZone','local','InputFormat','MM/dd/yyyy HH:mm');
% consts
Nt = 30*24*60/DURATION;
Nw = ceil(WE/GRID);
Nh = ceil(NS/GRID);


%% extract DS
clc; tic;

conn = sqlite('/Volumes/SSD/taxi.db','readonly');
DS = zeros(Nh,Nw,Nt); % DROPS SNAPSHOT
CURRENT_TIME = START_TIME;
for t = 1:Nt
    start_time_str = datestr(CURRENT_TIME,'yyyy-mm-dd HH:MM:SS');
    end_time_str = datestr(CURRENT_TIME + minutes(DURATION),'yyyy-mm-dd HH:MM:SS');
    query = sprintf('SELECT latitude,longitude FROM drops WHERE timestamp BETWEEN "%s" AND "%s" AND latitude BETWEEN %d AND %d AND longitude BETWEEN %d AND %d',...
            start_time_str,end_time_str,B,T,L,R);
    results = cell2mat(fetch(conn,query));
    hid = (T - results(:,1)) * Nh / tb;
    wid = (results(:,2) - L) * Nw / rl;
    cnt = 0;
    for i = 1:size(results,1)
        try
            DS(hid(i),wid(i),t) = DS(hid(i),wid(i),t) + 1;
        catch
            cnt = cnt + 1;
        end
    end
    fprintf('%s\t%s\t%d\t%d\n',start_time_str,end_time_str,i,cnt);
    CURRENT_TIME = CURRENT_TIME + minutes(DURATION);
end
toc;

save('DS','DS');
