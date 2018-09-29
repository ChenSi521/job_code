#!/usr/bin/env python
# _*_ coding:utf-8 -*-
import cv2
import numpy as np

txt_f = open('/home/chen/datasets/movie/10030101/movie_get/01030010_flip_cut/alldata.txt', 'r')
for line in txt_f.readlines()[435:440]:
    data = line.strip().split(' ')
    image_path = '/home/chen/datasets/movie/10030101/movie_get/01030010_flip_cut/' + data[0]
    image = cv2.imread(image_path)
    cv2.putText(image, data[0] + '|||||' +str(float(data[1]) * 180 / np.pi) + '|||||' + str(
        float(data[2]) * 180 / np.pi) + '|||||' + str(float(data[3]) * 180 / np.pi), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255))
    for i in range(68):
        cv2.circle(image, (int(float(data[4+i])), int(float(data[72+i]))), 2, (0, 255, 0))
    cv2.imshow('data[0]', image)
    if cv2.waitKey(0) & 0xFF == ord('0'):
        continue
cv2.destroyAllWindows()