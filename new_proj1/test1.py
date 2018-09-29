#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import os
import scipy.io as scio

#data_file = '/home/chen/Downloads/FaceProfilingRelease_v1.1/input/134212_1_face.mat'
data_file = '/home/chen/git-test/FaceProfilingRelease_v1.1/input/134212_1.mat'
data = scio.loadmat(data_file)
print(data)
#print(len(data['pts']))
print(len(data.keys()))
for i in data.keys():
    print(i)
#print(data['img'].shape)
print(data_file.replace("chen","chen1"))