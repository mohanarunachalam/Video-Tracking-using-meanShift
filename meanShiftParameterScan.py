# based on https://docs.opencv.org/trunk/db/df8/tutorial_py_meanshift.html
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

def ReadImage(i):
    filename = str(i)
    filename = filename.zfill(3)
    filename += '.png'
    img = cv2.imread(filename)
    return img

def GroundTruth(i):
    img = cv2.imread('001.png')
    (r1, r2, c1, c2) = (img.shape[0] / 2 - 95, img.shape[0] / 2 + 15, img.shape[1] / 2 - 5, img.shape[1] / 2 + 25)
    for i in range(2, i+1):
        if i < 10:
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
        if i > 88:
            r2 -= 2
    ground_truth = [c1, r1, c2, r2]
    return ground_truth

def FrameScore(ground_truth, track_window):
    # adapted from: https://stackoverflow.com/questions/27152904/calculate-overlapped-area-between-two-rectangles
    tw = np.zeros((4, 1))
    p1=[0,0]
    p2=[0,0]
    tw[0] = track_window[0]
    tw[1] = track_window[1]
    tw[2] = track_window[0] + track_window[2]
    tw[3] = track_window[1] + track_window[3]
    p1[0] = ground_truth[0] # row
    p1[1] = ground_truth[1] # column
    p2[0] = ground_truth[2] # row
    p2[1] = ground_truth[3]  # row
    set1 = set((r, c) for r, c in zip(range(p1[0], p2[0]), range(p1[1], p2[1])))
    set2 = set((r, c) for r, c in zip(range(tw[0], tw[2]), range(tw[1], tw[3])))
    score = len(set1.intersection(set2))
    return score


def RunInstance(r = 92,h = 38,c = 288,w = 26):
    print r, h, c, w
    frame = cv2.imread('001.png')
    # setup initial location of window
    track_window = (c,r,w,h)
    # set up the ROI for tracking
    roi = frame[r:r+h, c:c+w]
    mask = cv2.inRange(roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))
    roi_hist = cv2.calcHist([roi],[0],mask,[180],[0,180])
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)
    # Setup the termination criteria, either 10 iteration or move by atleast 1 pt
    term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )
    score = 0
    for i in range(2, 113):
        frame = ReadImage(i)
        dst = cv2.calcBackProject([frame],[0],roi_hist,[0,180],1)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        # Draw it on image
        x,y,w,h = track_window
        ground_truth = GroundTruth(i)
        score += FrameScore(ground_truth, track_window)
    return score

def PlotParameterScan(score):
    score = score.reshape(12, 12)
    fig = plt.figure()
    plot = fig.add_subplot(111)
    plot.imshow(score, cmap='hot')
    plot.axes.get_xaxis().set_visible(False)
    plot.axes.get_yaxis().set_visible(False)
    plot.set_title('Parameter Scan')
    fig.savefig('ParameterScan.png')


def RunCycle():
    s = []
    for r in range(88, 94, 2):
        for h in range(34, 40, 2):
            for c in range(286, 294, 2):
                for w in range(24, 32, 2):
                    score = RunInstance(r, h, c, w)
                    s.append(score)
    print s
    s = np.asarray(s)
    PlotParameterScan(s)
RunCycle()
#RunInstance('HSV new')