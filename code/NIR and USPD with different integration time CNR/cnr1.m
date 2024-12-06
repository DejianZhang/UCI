x1 = [0.1 1 2 3 4];
y1 = [0.6260 0.7237 0.6965 0.9606 1.011];

% 设置y轴范围从零开始
% 绘制折线图
plot(x1, y1, 'r-o', 'LineWidth', 1.5); % 绘制第一条线
hold on;  % 保持当前图

x2 = [0.1 1 2 3 4];
y2 = [1.5768 1.5125 1.5125 1.5394 1.6885];
% 绘制第二条线
plot(x2, y2, 'b-x', 'LineWidth', 1.5);
set(gcf,'Position',[100 100 400 300]);
% 设置图形属性
set(gca, 'FontName', 'Times New Roman', 'FontWeight', 'bold', 'FontSize', 14);
xlabel('Integration time(s)', 'FontSize', 16, 'FontName', 'Times New Roman', 'FontWeight', 'bold');
ylabel('CNR', 'FontSize', 16, 'FontName', 'Times New Roman', 'FontWeight', 'bold');

% 设置y轴范围
xlim([0,4.5]);
ylim([0,2.5]); xticks([0.1 1 2 3 4]);                                                     

% 显示图例
legend('NIR', 'USPD');

% 设置图形位置
ax = gca;
currentPosition = get(ax, 'Position'); 
newPosition = [0.19 0.19 0.74 0.74];
set(ax, 'Position', newPosition);

% 显示网格
grid off;
