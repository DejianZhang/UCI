relativePath = fullfile('..', '..', 'data', 'ingasn双层泡沫NCU0.1s时间门控+滤波器模式freeruning正常功率(1000)噪声(7700).mat');
load(relativePath);
G= zeros(size(rect_data,1), size(rect_data,2));
for m = 1:size(rect_data,1)
    for n=1:size(rect_data,2)
        b=rect_data(m,n,:);

        maxrect_data = sum(b(950:1200)); 

        G(m,n)=maxrect_data;
     end
end
A =log(G);
figure
%  imagesc(G);caxis([876, 7430]);axis off;
 T_min = min(A(:));
 T_max = max(A(:));
 T_normalized = (A - T_min) / (T_max - T_min);
 imagesc(T_normalized);axis off;
%  caxis([-0.5524, 1]);
 colormap('parula')