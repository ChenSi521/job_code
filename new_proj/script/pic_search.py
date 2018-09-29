#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path
import cv2
import numpy as np

pic_path = '/home/chen/datasets/5222.jpg'

work_path = '/home/chen/datasets/Smoke/destination/'

work_path_P = Path(work_path)
img_paths = work_path_P.rglob('*.jpg')
img0 = cv2.imread(pic_path)
img0_gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
#img0_gray = cv2.GaussianBlur(img0_gray, (5, 5), 0)
for num, img_path in enumerate(img_paths):
    img = cv2.imread(str(img_path))
    img = cv2.resize(img, (166, 166))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)

    framediff = cv2.absdiff(img_gray, img0_gray)
    framediff_bin = cv2.threshold(framediff, 10, 1, cv2.THRESH_BINARY)[1]
    #print(framediff_bin)
    #print(np.sum(framediff_bin))
    if num % 1000 == 0:
        print(num)

    if np.sum(framediff_bin) < 20:
        print(str(img_path))
        break


