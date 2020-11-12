prices = [0.7692 0.833;
0.7857 0.9167;
0.6667 0.5;
0.9 0.75;
0.6429 0.75;
0.6667 0.7273];

bar(prices)
set(gca,'xticklabel',{'SIFT','SURF','BRIEF', 'ORB','BRISK','FREAK'});
title('Precision and Recall comparison for "Dutch" dataset');
legend('Precision','Recall');

saveas(gcf,'Barchart.png')