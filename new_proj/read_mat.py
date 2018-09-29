#!/usr/bin/env python
# _*_ coding:utf-8 -*-
#!/usr/bin/env python
# _*_ coding:utf-8 -*-
import numpy as np
import scipy.io as scio
import cv2

data = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_0.mat')
data1 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_1.mat')
data2 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_2.mat')
data3 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_3.mat')
data4 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_4.mat')
data5 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_5.mat')
data6 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_6.mat')
data7 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_7.mat')
data8 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_8.mat')
data9 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_9.mat')
data10 = scio.loadmat('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_003_1_10.mat')
image = cv2.imread('/home/chen/datasets/300W_LP _1/IBUG/IBUG_image_106_0.jpg')
# print(image.shape)
# print(type(data))
# print(len(data.keys()))
# #print(data['Shape_Para'])
print(data['Pose_Para'])

#--------------------------------------------#
#all output is equal.
#ke yi kan chu:gao he kuan dou shi 470 ge xiang su.
print(data['roi'])
print(data1['roi'])
print(data2['roi'])
print(data3['roi'])
print(data4['roi'])
print(data5['roi'])
print(data6['roi'])
print(data7['roi'])
print(data8['roi'])
print(data9['roi'])
print(data10['roi'])
#---------------------------------------------#

#right_h = data['roi'][0]
for i in data.keys():
    print(i)
cv2.imshow('result.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# #print(data)

import os
p=os.listdir('/home/chen/datasets/300W_LP')
print(p)