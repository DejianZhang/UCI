relativePath = fullfile('..', '..', 'data', 'ppln双层泡沫NCU0.1s正常功率(1000)噪声(7700).mat');
load(relativePath);
G= zeros(size(rect_data,1), size(rect_data,2));
for m = 1:size(rect_data,1)
    for n=1:size(rect_data,2)
        b=rect_data(m,n,:);
        
        maxrect_data = sum(b(1233:1643));
        
        G(m,n)=maxrect_data;
    end
end
c=rect_data(4,12,:);
cc=reshape(c,1,2000);
cc_min = min(cc);
cc_max = max(cc);
cc_normalized = (cc - cc_min) / (cc_max - cc_min);
figure;
set(gcf,'Position',[100 100 400 300]);
n=length(cc_normalized);
x_new = 5 * (1:n)/1000;
plot(x_new,cc_normalized,'LineWidth', 1.5);
set(gca, 'FontName', 'Times New Roman','FontWeight','bold', 'FontSize', 14);
xlabel('Arrival Time(ns)', 'FontSize', 16, 'FontName', 'Times New Roman','FontWeight', 'bold');
ylabel('Normalized Photon Counts', 'FontSize', 16, 'FontName', 'Times New Roman','FontWeight', 'bold');
ylim([0 1.1]);xticks([0 2.5 5 7.5 10]);
ax = gca;
currentPosition = get(ax, 'Position');
newPosition = [0.19 0.19 0.74 0.74];
set(ax, 'Position', newPosition);
% plot(cc_normalized);