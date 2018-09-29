#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path
import re
import shutil

work_path = '/home/chen/datasets/Smoke/'
work_path_P = Path(work_path)

smoking_folders = work_path_P.rglob('Smoking*')
num_all = 0
for num, smoking_folder in enumerate(sorted(smoking_folders)):
    print num, str(smoking_folder)
    imgs = smoking_folder.glob('*')
    num_imgs = len([x for x in imgs])
    num_all += num_imgs
    print num_imgs
    # break
print num_all


