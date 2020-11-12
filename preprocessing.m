original = imread('original.png');
original = im2bw(original, 0.9);

subplot(1,2,1)
imshow(original);
se = strel('disk',5);

afterOpening = imopen(original,se);
se = strel('disk',1);
afterOpening = imclose(afterOpening,se);

subplot(1,2,2)
imshow(afterOpening,[]);

imwrite(afterOpening,'prep_original.png')









