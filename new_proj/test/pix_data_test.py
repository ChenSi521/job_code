#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import cv2
image_path = '/home/chen/datasets/movie/10030101/test1/01030010_flip_cut_aligned_Img_step/Img_csv_concat_step2/frame_det_00_001898.bmp'

image = cv2.imread(image_path)
print(type(image))
print(image[326, 242])
print(image[238, 220])
print(image[256, 240])
print(image[218, 245])
print(image[398, 254])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image[326, 242])  #第一个坐标是y，第二个坐标是x
print(image[238, 220])
print(image[256, 240])

cv2.imshow('1', image)
cv2.waitKey(10)
cv2.destroyAllWindows()

import numpy as np
import pandas as pd
ds = pd.Series([])
c = np.zeros((1, 1))
c = np.array([1,1,1])
print('a', c)


