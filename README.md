# VideoTracking
The code was written by Daniel Ziv and Ran Feldesh.
The code tracks a person across a few seconds video. 
The process:
1. each frame is extracted from the video (appears here as .png)
2. The region of interest (ROI) is defined by the user in code; the user defines a rectangle within the first frame, after which the code is aimed to follow on the following frames.
3. A color histogram is calculated for the ROI in the first frame.
4. Tracking begins for the next frame: a probability is calculated for each pixel, representing how likely it is to be part of the ROI, based on the correspondence of its color to the histogram (='backprojection'). 
5. With the backprojection image and the estimated location of the ROI in the previous frame, conduct a meanShift calculation: gradient ascent towards a local maximum - where the weighted mean is maximal (backprojection value weighted by inverse of the distance). Tracking ends for this frame, with output of the new estimated location of the ROI.
6. Repeat 4-5 for all frames in the video. The histogram is kept constant.

As with most algorithms, better results are achieved by optimizing hyperparameters. Here, optimization of the ROI location on the first frame and the color preprocess (before the backprojection) has been done, by automatic grid search, comparing performance to ground truth. The current code is sensitive to hyperparameters.

The original video:
https://youtu.be/xsNBbQVkIms
The optimized meanShift tracking results:
https://youtu.be/5rrXvel_DVc

For info about meanShift, see:
https://en.wikipedia.org/wiki/Mean_shift
https://docs.opencv.org/trunk/db/df8/tutorial_py_meanshift.html
https://youtu.be/hJg7ik4x95U
In addition to video processing, the meanShift algorithm can be used as a clustering algorithm, allocating basins of attraction of an arbitrary data (similar to SVM and k-means with respect to the output).
