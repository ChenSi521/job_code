#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import pandas as pd
import cv2
import numpy as np
import os

work_path = '/home/chen/datasets/movie/10030101/test1/01030010_flip_cut_aligned/'
work_path1 = '/home/chen/datasets/movie/10030101/test1/01030010_flip_cut_aligned_Img_step/'
csv_name = 'Img_csv_concat.csv'
step1_csv_name = 'Img_csv_concat_step1_0.csv'


landmarks_name_x = ['x_0', 'x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6', 'x_7', 'x_8', 'x_9', 'x_10', 'x_11', 'x_12', 'x_13', 'x_14', 'x_15', 'x_16', 'x_17', 'x_18', 'x_19', 'x_20', 'x_21', 'x_22', 'x_23', 'x_24', 'x_25', 'x_26', 'x_27', 'x_28', 'x_29', 'x_30', 'x_31', 'x_32', 'x_33', 'x_34', 'x_35', 'x_36', 'x_37', 'x_38', 'x_39', 'x_40', 'x_41', 'x_42', 'x_43', 'x_44', 'x_45', 'x_46', 'x_47', 'x_48', 'x_49', 'x_50', 'x_51', 'x_52', 'x_53', 'x_54', 'x_55', 'x_56', 'x_57', 'x_58', 'x_59', 'x_60', 'x_61', 'x_62', 'x_63', 'x_64', 'x_65', 'x_66', 'x_67']
landmarks_name_y = ['y_0', 'y_1', 'y_2', 'y_3', 'y_4', 'y_5', 'y_6', 'y_7', 'y_8', 'y_9', 'y_10', 'y_11', 'y_12', 'y_13', 'y_14', 'y_15', 'y_16', 'y_17', 'y_18', 'y_19', 'y_20', 'y_21', 'y_22', 'y_23', 'y_24', 'y_25', 'y_26', 'y_27', 'y_28', 'y_29', 'y_30', 'y_31', 'y_32', 'y_33', 'y_34', 'y_35', 'y_36', 'y_37', 'y_38', 'y_39', 'y_40', 'y_41', 'y_42', 'y_43', 'y_44', 'y_45', 'y_46', 'y_47', 'y_48', 'y_49', 'y_50', 'y_51', 'y_52', 'y_53', 'y_54', 'y_55', 'y_56', 'y_57', 'y_58', 'y_59', 'y_60', 'y_61', 'y_62', 'y_63', 'y_64', 'y_65', 'y_66', 'y_67']
data_names = ['confidence', 'pose_Ry']

image_save_path = work_path1 + step1_csv_name.split('.')[0] + '/'
if not os.path.exists(image_save_path):
    os.makedirs(image_save_path)
df = pd.read_csv(work_path1 + csv_name, header=0, sep=',', engine='python')
#dt = df[(df['confidence'] > 0.9) & (df['pose_Ry'] <= 0.52) & (df['pose_Ry'] >= -0.52) & (df['pose_Rx'] <= 0.45) & (df['pose_Rx'] >= -0.45)]
dt = df[(df['confidence'] > 0.95) & (df['pose_Ry'] <= 0.05) & (df['pose_Ry'] >= -0.05) & (df['pose_Rx'] <= 0.45) & (df['pose_Rx'] >= -0.45)]
dt.to_csv(work_path1 + step1_csv_name, index=0)

frame_names = list(dt['frame_name'])
print(frame_names[0])
for frame_name in frame_names:
    frame_path = work_path + frame_name + '.bmp'
    #print(frame_path)
    image = cv2.imread(frame_path)
    row = dt[dt.frame_name == frame_name].index.tolist()[0]
    #print(row)
    landmarks_x = list(dt.loc[row, landmarks_name_x])
    # print(landmarks_x)
    landmarks_y = list(dt.loc[row, landmarks_name_y])
    data_others = list(dt.loc[row, data_names])
    cv2.putText(image,
                frame_name + '||' + str(data_others[0]) + '||' + str(data_others[1]),
                (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
    for i in range(68):
        cv2.circle(image, (int(landmarks_x[i]), int(landmarks_y[i])), 2, (0, 255, 0))
    cv2.imshow('image_with_dot', image)
    cv2.imwrite(image_save_path + frame_name + '.bmp', image)
    cv2.waitKey(10)
cv2.destroyAllWindows()

