#!/usr/bin/env python
# _*_ coding:utf-8 -*-

#!/usr/bin/env python
# _*_ coding:utf-8 -*-

#!/usr/bin/env python
# _*_ coding:utf-8 -*-
from pathlib import Path
import cv2
import numpy as np
from scipy.spatial import distance as dist
import shutil
import os

SCIPY_METHODS = (
    ("Euclidean", dist.euclidean),
    ("Manhattan", dist.cityblock),
    ("Chebysev", dist.chebyshev))

all_pics = []

a = '/home/chen/datasets/Taking phone/Call Clash Prank _ Prank In India ( Part -2 ) _ The crazy sumit'

work_path = a + '/part_1/'
work_path_save = a +'/part_1/1/'
#work_path = '/home/chen/datasets/www/'
#work_path_save = '/home/chen/datasets/www/1/'

if not os.path.exists(work_path_save):
    os.makedirs(work_path_save)

work_path_P = Path(work_path)
img_paths = work_path_P.glob('*.jpg')


sig = 0
for num, img_path in enumerate(sorted(img_paths, cmp=lambda x, y: len(x.name) - len(y.name))):
    #print(str(img_path))
    img = cv2.imread(str(img_path))
    img = cv2.resize(img, (166, 166))
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([img], [0, 1, 2], None, [128, 128, 128], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    if num % 100 == 0:
        print(num)
    if num == 2501:
        break
    if len(all_pics) > 0:
        for pic_list in reversed(all_pics):
            if len(pic_list) > 0:
                for img_path_pre in [pic_list[-1]]:
                    img_pre = cv2.imread(img_path_pre)
                    img_pre = cv2.resize(img_pre, (166, 166))
                    #img_pre_gray = cv2.cvtColor(img_pre, cv2.COLOR_BGR2GRAY)
                    hist_pre = cv2.calcHist([img_pre], [0, 1, 2], None, [128, 128, 128], [0, 256, 0, 256, 0, 256])
                    hist_pre = cv2.normalize(hist_pre, hist_pre).flatten()
                    d = dist.euclidean(hist, hist_pre)
                    #framediff = cv2.absdiff(img_gray, img_pre_gray)
                    #framediff_bin = cv2.threshold(framediff, 150, 1, cv2.THRESH_BINARY)[1]
                    # if np.sum(framediff_bin) < 1000:
                    #
                    #     pic_list.append(str(img_path))
                    #     sig = 1
                    #     break
                    #print(str(img_path), img_path_pre, d)
                    if d < 0.85:
                        pic_list.append(str(img_path))
                        sig = 1
                        break

                else:
                    continue
                break
    if sig == 0:
        #print(str(img_path))
        all_pics.append([str(img_path)])
    sig = 0
    #print(all_pics)
#print(all_pics)

shuzi = 0
if len(all_pics) > 0:
    for pic_list in all_pics:
        if len(pic_list) > 0:
            for img_path in pic_list:
                #img = cv2.imread(img_path)
                #cv2.imwrite(work_path_save + str(shuzi) + '.jpg', img)
                shutil.move(img_path, work_path_save + str(shuzi) + '.jpg')
                shuzi += 1


