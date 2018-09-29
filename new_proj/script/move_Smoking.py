#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path
import re
import shutil

work_path = 'smb://dog/public/people/fqchen/Smoking/'
#work_path = 'smb://10.6.0.6/public/people/fqchen/Smoking/test/'
work_path_P = Path(work_path)
work_path_sorted = 'smb://dog/public/people/fqchen/Smoking/sorted/'
work_path_sorted_P = Path(work_path_sorted)

smoking_folders = work_path_P.glob('*')
num_imgs = len([x for x in smoking_folders])
print(num_imgs)

'''
num_all = 0
for num, smoking_folder in enumerate(sorted(smoking_folders)):
    print num, str(smoking_folder)
    imgs = smoking_folder.glob('*')
    num_imgs = len([x for x in imgs])
    if num_imgs != 0:
        for img in imgs:
            if not (work_path_sorted_P/(img.parent.parent.name)).exists():
                (work_path_sorted_P / (img.parent.parent.name)).mkdir(parents=True)
            shutil.copy(str(img), str(work_path_sorted_P/(img.parent.parent.name)))
    num_all += num_imgs
    print num_imgs
    # break
print num_all
'''
