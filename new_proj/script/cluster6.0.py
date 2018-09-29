#!/usr/bin/env python
# _*_ coding:utf-8 -*-

#这个是参数和效果都比较好的一个版本，即使修改，尽量别在这个版本上修改。
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


a = '/home/chen/datasets/Taking phone fromed/CELL PHONE CRASHING at a PARK!'   #最后位置不带斜杠

part_num = 'part_1'

class_choice = ['other_max', 'other_min', 'talking_max', 'talking_min']

for clas in class_choice:
    for zero_one in range(2):
# zero_one = 0
# #zero_one = 1
        work_path = a + '/' + part_num + '/' + clas

        work_path_save = work_path + '/' + str(zero_one) + '/'
        #work_path = '/home/chen/datasets/www/'
        #work_path_save = '/home/chen/datasets/www/1/'

        all_pics = []

        #work_path_save = work_path_save + str(num % 2000) + '/'
        if not os.path.exists(work_path_save):
            os.makedirs(work_path_save)

        work_path_P = Path(work_path)
        img_paths = work_path_P.glob('*.jpg')

        sig = 0

        for num, img_path in enumerate(sorted(img_paths, cmp=lambda x, y: int(x.name[:-4]) - int(y.name[:-4]))):
        #for num, img_path in enumerate(sorted(img_paths, cmp=lambda x, y: int((float(x.name[:-11]) - float(y.name[:-11]))*100000000))):
            #print(str(img_path))
            img = cv2.imread(str(img_path))
            img = cv2.resize(img, (166, 166))
            #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            hist = cv2.calcHist([img], [0, 1, 2], None, [128, 128, 128], [0, 256, 0, 256, 0, 256])
            hist = cv2.normalize(hist, hist).flatten()
            if num % 100 == 0:
                print(num)
            if num == 2500:
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
                            #if d < 0.85:
                            if d < 0.75:
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

            #if len(all_pics)%100 == 0:
        shuzi = 0
        if len(all_pics) > 0:
            for pic_list in all_pics:
                if len(pic_list) > 0:
                    for img_path in pic_list:
                        #img = cv2.imread(img_path)
                        #cv2.imwrite(work_path_save + str(shuzi) + '.jpg', img)
                        shutil.move(img_path, work_path_save + str(shuzi) + '.jpg')
                        shuzi += 1
#         all_pics = []
# #print(all_pics)
# if len(all_pics) > 0:
#     for pic_list in all_pics:
#         if len(pic_list) > 0:
#             for img_path in pic_list:
#                 #img = cv2.imread(img_path)
#                 #cv2.imwrite(work_path_save + str(shuzi) + '.jpg', img)
#                 shutil.move(img_path, work_path_save + str(shuzi) + '.jpg')
#                 shuzi += 1






