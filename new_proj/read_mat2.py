#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import numpy as np
import scipy.io as scio
import cv2

data = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_106_0.mat')
image = cv2.imread('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_106_0.jpg')
#print(data)
# print(type(data))
print(len(data.keys()))
#print(data['roi'])
print(len(data['pt2d'][0]))
print(len(data['pt2d'][1]))
print(data['pt2d'][0])
print(data['pt2d'][1])
for i in data.keys():
   print(i)
#print(data)
cv2.imshow('result.jpg', image)
cv2.waitKey(0)
#cv2.destroyAllWindows()