#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import scipy.io as scio
import cv2

data = scio.loadmat('/home/chen/datasets/300W_LP_1/IBUG/IBUG_image_106_5.mat')
image = cv2.imread('/home/chen/datasets/300W_LP_1/IBUG/IBUG_image_106_5.jpg')


for i in range(68):
    cv2.circle(image,(int(data['pt2d'][0][i]),int(data['pt2d'][1][i])),3,(0,0,255),-1)
cv2.imshow('result.jpg',image)
cv2.waitKey(0)
# cv2.circle()
# print('/'.join('/home/chen/datasets/300W_LP_1/IBUG/IBUG_image_106_0.mat'.split('/')[1:-2]))
# a='/home/chen/datasets/300W_LP_1/IBUG/IBUG_image_106_0.mat'.split('/')
# a[4] = '300W_LP_face'
# print(a[-3:])
# print(image.shape)
# print(a)
# num = input('111')
# if num == 0:
#     print("hhhhhh")