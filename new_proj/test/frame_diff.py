#!/usr/bin/env python
# _*_ coding:utf-8 -*-
from pathlib import Path
import pandas as pd
import cv2
import numpy as np

work_path = '/home/chen/datasets/movie_face/Female_mirror/1-FemaleNoGlasses-Normal_aligned/'
work_path_P = Path(work_path)

bmp_paths = (work_path_P.rglob('*bmp'))
ds = pd.Series([])
print(ds)
for num, bmp_path in enumerate(sorted(bmp_paths)):   #即使是生成器，也可以用sorted()很神奇。
    if num == 0:
        pre_bmp_path = str(bmp_path)
        continue
    else:
        bmp_path_str = str(bmp_path)
        image = cv2.imread(bmp_path_str)
        image = image[60:200, 60:200]
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image_gray = cv2.GaussianBlur(image_gray, (5, 5), 0)
        image_pre = cv2.imread(pre_bmp_path)
        image_pre = image_pre[60:200, 60:200]
        image_pre_gray = cv2.cvtColor(image_pre, cv2.COLOR_BGR2GRAY)
        image_pre_gray = cv2.GaussianBlur(image_pre_gray, (5, 5), 0)

        framediff = cv2.absdiff(image_gray, image_pre_gray)
        framediff_bin = cv2.threshold(framediff, 35, 1, cv2.THRESH_BINARY)[1]
        print(framediff_bin)
        # t = 0
        # for i in range(framediff_bin.shape[1]):
        #     for j in range(framediff_bin.shape[1]):
        #         if framediff_bin[i,j] > 0:
        #             t +=1
        #
        # print(t)
        print(np.sum(framediff_bin))
        pre_bmp_path = str(bmp_path)
    ds[num+1] = np.sum(framediff_bin)

    # if num == 1:
    #     break
ds.to_csv(work_path + 'diff.csv')