relativePath = fullfile('..', '..', 'data', 'ppln双层泡沫NCU4s正常功率(1000)噪声(7700).mat');
load(relativePath);
G= zeros(size(rect_data,1), size(rect_data,2));
for m = 1:size(rect_data,1)
    for n=1:size(rect_data,2)
        b=rect_data(m,n,:);
        
        maxrect_data = sum(b(1233:1643));
        
        G(m,n)=maxrect_data;
    end
end
A = log(G);
T_min = min(A(:));
T_max = max(A(:));
T_normalized = (A - T_min) / (T_max - T_min);
% T_normalized = G/(T_max);
%   T_normalized1= abs(1-T_normalized);
figure
imagesc(T_normalized);axis off;
colormap('parula')
% caxis([0,1])
% colorbar;