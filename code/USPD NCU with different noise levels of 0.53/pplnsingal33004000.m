relativePath = fullfile('..', '..', 'data', 'ppln双层泡沫NCU0.1s正常功率(1000)噪声(积分3300-4000)1.mat');
load(relativePath);
G= zeros(size(rect_data,1), size(rect_data,2));
for m = 1:size(rect_data,1)
    for n=1:size(rect_data,2)
        b=rect_data(m,n,:);
        
        maxrect_data = sum(b(1320:1540));
        
        G(m,n)=maxrect_data;
    end
end
A = log(G);
T_min = min(A(:));
T_max = max(A(:));
T_normalized = (A - T_min) / (T_max - T_min);
figure
imagesc(T_normalized);axis off;
colormap('parula')