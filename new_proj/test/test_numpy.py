#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import numpy as np

xx = np.array([[2.0,3.0],[4.0,5.0]])
yy = np.array([[0.2,0.3],[0.4,0.5]])
a = np.array([6.0])
s = xx[:,1] *yy[:,1]
print(s)
gg = np.maximum(a[0],xx[:,1])

print(gg*gg)

for i in xx:
    print(i)
    print(i.reshape(1,-1))
print("..")
for i,m in enumerate(xx):
    print(m)
b = np.zeros((2,2))
a = (1,2)
b[0] = a
b[1] = a
print(b.reshape(4))
print(a)


a = [[1,1,'t'], ['4', 'd','g']]
print(a[1].index('d'))
landmarks_name = [' x_0', ' x_1', ' x_2', ' x_3', ' x_4', ' x_5', ' x_6', ' x_7', ' x_8', ' x_9', ' x_10', ' x_11', ' x_12', ' x_13', ' x_14', ' x_15', ' x_16', ' x_17', ' x_18', ' x_19', ' x_20', ' x_21', ' x_22', ' x_23', ' x_24', ' x_25', ' x_26', ' x_27', ' x_28', ' x_29', ' x_30', ' x_31', ' x_32', ' x_33', ' x_34', ' x_35', ' x_36', ' x_37', ' x_38', ' x_39', ' x_40', ' x_41', ' x_42', ' x_43', ' x_44', ' x_45', ' x_46', ' x_47', ' x_48', ' x_49', ' x_50', ' x_51', ' x_52', ' x_53', ' x_54', ' x_55', ' x_56', ' x_57', ' x_58', ' x_59', ' x_60', ' x_61', ' x_62', ' x_63', ' x_64', ' x_65', ' x_66', ' x_67', ' y_0', ' y_1', ' y_2', ' y_3', ' y_4', ' y_5', ' y_6', ' y_7', ' y_8', ' y_9', ' y_10', ' y_11', ' y_12', ' y_13', ' y_14', ' y_15', ' y_16', ' y_17', ' y_18', ' y_19', ' y_20', ' y_21', ' y_22', ' y_23', ' y_24', ' y_25', ' y_26', ' y_27', ' y_28', ' y_29', ' y_30', ' y_31', ' y_32', ' y_33', ' y_34', ' y_35', ' y_36', ' y_37', ' y_38', ' y_39', ' y_40', ' y_41', ' y_42', ' y_43', ' y_44', ' y_45', ' y_46', ' y_47', ' y_48', ' y_49', ' y_50', ' y_51', ' y_52', ' y_53', ' y_54', ' y_55', ' y_56', ' y_57', ' y_58', ' y_59', ' y_60', ' y_61', ' y_62', ' y_63', ' y_64', ' y_65', ' y_66', ' y_67']
landmarks_col_num = [ landmarks_name.index(xxx) for xxx in landmarks_name]
print(landmarks_col_num)

import os

print(os.path.isfile('/home/chen/datasets/movie/01/10030112/flip_video'))

name = 'frame_det_00_000027.bmp'
name_l = name.split('.')[-2].split('_')[-1]
print(int(float(name_l)))