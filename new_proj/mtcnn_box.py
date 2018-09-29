#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import mxnet as mx
from mtcnn_detector import MtcnnDetector
import cv2
import os
import time

detector = MtcnnDetector(model_folder='model', ctx=mx.cpu(0), num_worker = 4 , accurate_landmark = True)

image = cv2.imread('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_106_0.jpg')
results = detector.detect_face(img)
if results is not None:
    total_boxes = results[0]
    points = results[1]
    cv2.circle(image,(total_boxes[0][0],total_boxes[0][1]),3,(0,0,255),-1)
    cv2.circle(image, (total_boxes[0][2], total_boxes[0][3]), 3, (0, 0, 255), -1)

cv2.imshow('result.jpg',image)
cv2.waitKey(0)
cv2.circle()