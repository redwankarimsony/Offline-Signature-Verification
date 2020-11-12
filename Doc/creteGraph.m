img = imread('C:\Users\Redwan Karim Sony\Desktop\Simulation\13_049.PNG');
imgGray = rgb2gray(img);
% imgGray = img;

corners = detectHarrisFeatures(imgGray);
figure(1),
imshow(imgGray); hold on;
points = corners.selectStrongest(30);
plot(points); hold on;

x = double(points.Location(:,1));
y = double(points.Location(:,2));

TRI = delaunay(x,y);
triplot(TRI,x,y);
figure (2);
triplot(TRI,x,y);
