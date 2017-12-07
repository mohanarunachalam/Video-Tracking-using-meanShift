import matplotlib.pyplot as plt

for i in range(1, 112):
    filename = str(i)
    if len(filename)==1:
        filename = '00' + filename + '.png'
    if len(filename) == 2:
        filename = '0' + filename + '.png'
    if len(filename) == 3:
        filename = filename + '.png'
    img = plt.imread(filename)
    plt.imshow(img)
    plt.show(block=False)
    plt.pause(0.02)