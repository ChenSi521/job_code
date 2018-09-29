#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import pandas as pd
import numpy as np
import scipy.io as scio

pic_path = '/home/chen/datasets/workflow_test/mat_genera_one/without_dot/frame_det_00_000400.bmp'
csv_path = '/home/chen/datasets/workflow_test/mat_genera_one/with_dot/frame_det_00_000400.csv'
pic_name_prefix = pic_path.split('/')[-1].split('.')[0]
print(pic_name_prefix)

df = pd.read_csv(csv_path, header=0, sep=', ', engine='python')
landmarks_name_x = ['x_0', 'x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6', 'x_7', 'x_8', 'x_9', 'x_10', 'x_11', 'x_12', 'x_13', 'x_14', 'x_15', 'x_16', 'x_17', 'x_18', 'x_19', 'x_20', 'x_21', 'x_22', 'x_23', 'x_24', 'x_25', 'x_26', 'x_27', 'x_28', 'x_29', 'x_30', 'x_31', 'x_32', 'x_33', 'x_34', 'x_35', 'x_36', 'x_37', 'x_38', 'x_39', 'x_40', 'x_41', 'x_42', 'x_43', 'x_44', 'x_45', 'x_46', 'x_47', 'x_48', 'x_49', 'x_50', 'x_51', 'x_52', 'x_53', 'x_54', 'x_55', 'x_56', 'x_57', 'x_58', 'x_59', 'x_60', 'x_61', 'x_62', 'x_63', 'x_64', 'x_65', 'x_66', 'x_67']
landmarks_name_y = ['y_0', 'y_1', 'y_2', 'y_3', 'y_4', 'y_5', 'y_6', 'y_7', 'y_8', 'y_9', 'y_10', 'y_11', 'y_12', 'y_13', 'y_14', 'y_15', 'y_16', 'y_17', 'y_18', 'y_19', 'y_20', 'y_21', 'y_22', 'y_23', 'y_24', 'y_25', 'y_26', 'y_27', 'y_28', 'y_29', 'y_30', 'y_31', 'y_32', 'y_33', 'y_34', 'y_35', 'y_36', 'y_37', 'y_38', 'y_39', 'y_40', 'y_41', 'y_42', 'y_43', 'y_44', 'y_45', 'y_46', 'y_47', 'y_48', 'y_49', 'y_50', 'y_51', 'y_52', 'y_53', 'y_54', 'y_55', 'y_56', 'y_57', 'y_58', 'y_59', 'y_60', 'y_61', 'y_62', 'y_63', 'y_64', 'y_65', 'y_66', 'y_67']

arr_landmark = np.zeros((68, 2))

landmarks_x = list(df.loc[0, landmarks_name_x])
landmarks_y = list(df.loc[0, landmarks_name_y])
for i, xy in enumerate(zip(landmarks_x, landmarks_y)):
    arr_landmark[i] = xy
mat_name = pic_name_prefix + '.mat'
mat_path = '/'.join(pic_path.split('/')[:-1]) + '/' + mat_name
scio.savemat(mat_path, {'pts': arr_landmark})


