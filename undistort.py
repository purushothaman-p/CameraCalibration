import cv2
import numpy as np

# Load the calibration data from npz file
np_data = np.load('calib.npz')
mtx = np_data['arr_0']
dist =  np_data['arr_1']

# print the matrices
print(mtx)
print(dist)

# read the file to be undistorted
img = cv2.imread('1.jpg')
h, w = img.shape[:2]

newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

x, y, w, h = roi
dst = img[y:y+h, x:x+w]

#display the undistorted image
cv2.imshow('undistorted', dst)
cv2.waitKey()
cv2.destroyAllWindows()
