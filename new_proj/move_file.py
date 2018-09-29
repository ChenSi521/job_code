#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import shutil
import os

path_parnt = '/home/chen/datasets/300W_LP'
path = os.listdir(path_parnt)
for i in path:
    path_fold = path_parnt + '/' + i + '/' + 'mix_detected_face'
    if os.path.exists(path_fold):
        file_name = os.listdir(path_fold)
        for m in file_name:
            shutil.move(path_fold+'/'+m, path_parnt+'/'+i)

