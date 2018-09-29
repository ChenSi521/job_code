#!/usr/bin/env python
# _*_ coding:utf-8 -*-
import cv2
import numpy as np
import os


work_path = '/home/chen/datasets/movie/10030101/'
video_name = '01030010_flip_cut.avi'

#work_path = '/home/chen/git-test/OpenFace-master/build/processed/'
#video_name = 'webcam_2018-07-30-13-43.avi'

video_cores_file = work_path + video_name.split('.')[0] + '/'
crop_image_txt_path = video_cores_file + 'crop_image_txt/'
txt_f = open(crop_image_txt_path + 'alldata.txt', 'r')
crop_image_landmark_path = video_cores_file + 'crop_image_landmark/'
if not os.path.exists(crop_image_landmark_path):
    os.makedirs(crop_image_landmark_path)
line_num = 0
for line in txt_f.readlines():
    line_num +=1
    data = line.strip().split(' ')
    if not os.path.exists(crop_image_landmark_path):
        os.makedirs(crop_image_landmark_path)
    image_path = crop_image_txt_path + data[0]
    image = cv2.imread(image_path)
    cv2.putText(image, data[0] + '||' + str(line_num) + '||' + data[1], (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
    cv2.putText(image, str(float(data[2]) * 180 / np.pi) + '||' + str(
        float(data[3]) * 180 / np.pi) + '||' + str(float(data[4]) * 180 / np.pi), (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
    for i in range(68):
        cv2.circle(image, (int(float(data[5+i])), int(float(data[73+i]))), 2, (0, 255, 0))
    cv2.imshow('data[0]', image)
    cv2.imwrite(crop_image_landmark_path + data[0], image)
    cv2.waitKey(10)
cv2.destroyAllWindows()