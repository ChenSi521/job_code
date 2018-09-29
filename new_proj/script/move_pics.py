#!/usr/bin/env python
# _*_ coding:utf-8 -*-
from pathlib import Path
import shutil
import os

work_path = '/home/chen/datasets/Smoke/Smoke_frame/Camel Turkish Royal Cigarette Review/Non-Smoking'
work_path = '/home/chen/datasets/Taking phone filted/CELL PHONE CRASHING at the AIRPORT!/other_max/'
work_path1 = '/home/chen/datasets/Smoke/Smoke_frame/Camel Turkish Royal Cigarette Review/'
work_path1 = work_path
work_path_P = Path(work_path)
work_path1_P = Path(work_path1)

# if not os.path.exists(work_path):
#     os.makedirs(work_path)

imgs = work_path1_P.glob('*.jpg')

for num, img in enumerate(imgs):
    if num%2000 != 0:
        shutil.move(str(img), work_path)
    else:
        work_path = work_path1 + str(num/2000) + '/'
        if not os.path.exists(work_path):
            os.makedirs(work_path)
        shutil.move(str(img), work_path)


