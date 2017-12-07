import matplotlib.pyplot as plt

for i in range(1, 40):
    filename = str(i)
    if len(filename)==1:
        filename = '00' + filename + '.png'
    if len(filename) == 2:
        filename = '0' + filename + '.png'
    if len(filename) == 3:
        filename = filename + '.png'
    img = plt.imread(filename)
    (r1,r2,c1,c2) = (img.shape[0] / 2 - 100, img.shape[0] / 2 - 80,img.shape[1] / 2 - 10, img.shape[1] / 2 + 10)
    imgTracked = img
    imgTracked[r1:r2, c1:c2, :] = 0
    plt.imshow(imgTracked)
    plt.show(block=False)
    plt.pause(0.02)