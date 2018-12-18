# CameraCalibration
Finding the camera matrix using openCV

### Refer:[OpenCV-Python Tutorials](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html)

## Usage:
Print the given Checker board pattern and stick it on a flat surface. Keep the camera in a stable position and take multiple pictures(15-20) with different orientations of the board. Save all the images in the directory of the code in .jpg format.

Run `python calibration.py`. It calculates the matrices and stores in `calib.npz`
Run `python undistort.py` by editing the file name in the code to get the undistorted image.
