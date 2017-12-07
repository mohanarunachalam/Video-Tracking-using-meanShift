# based on https://docs.opencv.org/trunk/db/df8/tutorial_py_meanshift.html
import numpy as np
import cv2
import os

def ReadImage(i):
    filename = str(i)
    if len(filename) == 1:
        filename = '00' + filename + '.png'
    if len(filename) == 2:
        filename = '0' + filename + '.png'
    if len(filename) == 3:
        filename = filename + '.png'
    img = cv2.imread(filename)
    return img
def RunInstance(directory = None, r = 90,h = 36,c = 282,w = 22):
    print r, h, c, w, directory
    frame = cv2.imread('001.png')
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    # setup initial location of window
    track_window = (c,r,w,h)
    # set up the ROI for tracking
    roi = frame[r:r+h, c:c+w]
    hsv_roi = roi
    #hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) #***
    mask = cv2.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
    for i in range(1, 112):
        frame = ReadImage(i)
        hsv = frame
        #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #***
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        #cv2.imshow('img2',img2)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            if directory:
                cv2.imwrite(directory + '/meanShift' + str(i)+".jpg",img2)
                if i == 1:
                    cv2.imwrite(directory + '/meanShift' + str(i) + ' r' + str(r) + 'h' + str(h) + ' c' + str(c) + 'w' + str(w) +".jpg", img2)
        cv2.destroyAllWindows()

def RunCycle():
    for r in range(90, 91, 1):
        for h in range(34, 44, 2):
            for c in range(282, 283, 1):
                for w in range(22, 36, 2):
                    directory = 'RGB r' + str(r) + ' h' + str(h) + ' c' + str(c) + ' w' + str(w)
                    RunInstance(directory, r, h, c, w)

RunCycle()
#RunInstance('RGB try4')