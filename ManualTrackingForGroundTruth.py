import cv2

def ReadImage(i):
    filename = str(i)
    filename = filename.zfill(3)
    filename = filename + '.png'
    img = cv2.imread(filename)
    return img

img = ReadImage(1)
(r1, r2, c1, c2) = (img.shape[0] / 2 - 95, img.shape[0] / 2 + 15, img.shape[1] / 2 - 5, img.shape[1] / 2 + 25)
img_w_target = cv2.rectangle(img, (c1, r1), (c2, r2), 255, 2)
cv2.imwrite('FixedPoint' + str(1).zfill(3) + ".jpg", img_w_target)
#cv2.imshow('img_w_target', img_w_target)
k = cv2.waitKey(60) & 0xff
for i in range(2, 113):
    img = ReadImage(i)
    if i<10:
        (c1, c2) = (c1 - 2, c2 - 2)
    if (i > 10) & (i < 20):
        (c1, c2) = (c1 - 1, c2 - 1)
    if (i > 21) & (i < 40):
        (c1, c2) = (c1 + 1, c2 + 1)
    if (i > 41) & (i < 53):
            (c1, c2) = (c1 + 3, c2 + 3)
    if (i > 72) & (i < 83):
        (c1, c2) = (c1 + 2, c2 + 2)
    if (i > 94) & (i < 100):
        (c1, c2) = (c1 - 5, c2 - 5)
    if (i > 101) & (i < 104):
        (c1, c2) = (c1 - 3, c2 - 3)
    if (i > 105) & (i < 113):
            (c1, c2) = (c1 - 5, c2 - 5)
    if i>88:
        r2 -= 2
    img_w_target = cv2.rectangle(img, (c1, r1), (c2, r2), 255, 2)
    cv2.imwrite('FixedPoint' + str(i).zfill(3) + ".jpg", img_w_target)
    #cv2.imshow('img_w_target', img_w_target)
    k = cv2.waitKey(60) & 0xff
cv2.destroyAllWindows()