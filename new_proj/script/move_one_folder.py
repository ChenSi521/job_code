#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import shutil
from pathlib import Path

work_path = '/home/chen/datasets/Smoke/Smoke_frame/Smoking/'
work_path1 = '/home/chen/datasets/Smoke/Smoke_frame/Camel Turkish Royal Cigarette Review/'

shutil.move(work_path, work_path1)