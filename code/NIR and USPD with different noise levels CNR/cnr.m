x = [ 0.13  0.3766 0.526 0.6753 0.7597 0.84 0.89];
y1 = [ 2.2373 2.1497 2.0096 1.7488 1.5024 1.1953 0.5906];
% 绘制第一条折线图
plot(x, y1, 'r-o', 'LineWidth', 1.5);
hold on;

% 第二组数据
 y2 = [ 1.7453 1.5168 1.5978 1.5292 1.5943 1.6431 1.5802];
% 绘制第二条折线图
plot(x, y2, 'b-x', 'LineWidth', 1.5);

% 设置图形属性
set(gca, 'FontName', 'Times New Roman', 'FontWeight', 'bold', 'FontSize', 14);
xlabel('Intensity', 'FontSize', 16, 'FontName', 'Times New Roman', 'FontWeight', 'bold');
ylabel('CNR', 'FontSize', 16, 'FontName', 'Times New Roman', 'FontWeight', 'bold');

% 设置y轴范围并确保显示4.5
ylim([0.5, 2.5]);
% yticks([0 1 2 3 4 5]);

% 设置x轴刻度
% xticks([0.2 0.4 0.6 0.8 1]);
xlim([0.1, 1]);
% 显示图例
legend('NIR', 'USPD');

% 调整图形窗口大小和位置
set(gcf, 'Position', [100 100 400 300]);

% 调整轴位置，以确保图像内容完全显示
ax = gca;
currentPosition = get(ax, 'Position');
newPosition = [0.19 0.19 0.74 0.74];
set(ax, 'Position', newPosition);

% 显示网格
grid off;

