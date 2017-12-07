import cv2
import time
import matplotlib.pyplot as plt

for i in range(1, 112):
    filename = str(i)
    if len(filename)==1:
        filename = '00' + filename + '.png'
    if len(filename) == 2:
        filename = '0' + filename + '.png'
    if len(filename) == 3:
        filename = filename + '.png'
    #print filename
    img = cv2.imread(filename)
    #print img
    #print type(img)
    #print img.shape
    plt.imshow(img)
    plt.show()
    time.sleep(0.03)