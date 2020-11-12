%%%%------------- Precision + Recall (Dutch)-----------------%
% prices = [0.7692 0.833;
% 0.7857 0.9167;
% 0.6667 0.5;
% 0.9 0.75;
% 0.6429 0.75;
% 0.6667 0.7273];
% 
% bar(prices)
% set(gca,'xticklabel',{'SIFT','SURF','BRIEF', 'ORB','BRISK','FREAK'});
% title('Precision and Recall comparison for "Dutch" dataset');
% legend('Precision','Recall');
% 
% saveas(gcf,'precision_recall_Dutch.png')
% saveas(gcf,'precision_recall_Dutch','epsc');

%%%%------------- Precision + Recall (Chinese)-----------------%

prices = [0.7857	0.9167;
0.8462	0.9167;
0.875	0.5833;
0.8333	0.8333;
0.8182	0.75;
0.7692	0.8333];

bar(prices)
set(gca,'xticklabel',{'SIFT','SURF','BRIEF', 'ORB','BRISK','FREAK'});
title('Precision and Recall comparison for "Chinese" dataset');
legend('Precision','Recall');

saveas(gcf,'precision_recall_Chinese.png')
saveas(gcf,'precision_recall_Chinese','epsc');



