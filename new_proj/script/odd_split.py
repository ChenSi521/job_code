#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import shutil
import os
import numpy as np

a = '/home/chen/datasets/Smoke/destination/dest_CleanImage/'

p = 'L&M - Red HARD SMOKE ft'

path = a + p + '/over_one/'
even_path = a + p + '/over_one/' + 'even/'
odd_path = a + p + '/over_one/' + 'odd/'

if not os.path.exists(even_path):
    os.makedirs(even_path)
if not os.path.exists(odd_path):
    os.makedirs(odd_path)

img_names = os.listdir(path)
for img_name in img_names:
    print(path+img_name)
    if os.path.isfile(path + img_name):
        img_num = int((img_name.split('/')[-1]).split('.')[0])
        if img_num%2 == 0:
            shutil.move(path + img_name, even_path)
        else:
            shutil.move(path + img_name, odd_path)

# def test():
#     print(np.array([1, 2]))