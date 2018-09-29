#!/usr/bin/env python
# _*_ coding:utf-8 -*-
import numpy as np
import scipy.io as scio

data = scio.loadmat('/home/chen/datasets/300W_LP/IBUG/IBUG_image_003_1_10.mat')
#data = scio.loadmat('/home/chen/datasets/300W_LP/Code/ModelGeneration/model_info.mat')
#print(data)
print(type(data))
print(len(data.keys()))
# #print(data['Shape_Para'])
# print(data['Pose_Para'])
for i in data.keys():
    print(i)
print(data['Shape_Para'].shape)
print(data['Pose_Para'])
#print(data)