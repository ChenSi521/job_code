#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import csv
import cv2
import numpy as np
import os

work_path = '/home/chen/datasets/movie/10030101/'
video_name = '01030010_flip_cut.avi'

# work_path = '/home/chen/git-test/OpenFace-master/build/processed/'
# video_name = 'webcam_2018-07-30-13-43.avi'

video_path = work_path + video_name
video_cores_file = work_path + video_name.split('.')[0] + '/'
openface_processed = video_cores_file + 'openface_processed/'
csv_name = video_name.split('.')[0] + '.csv'
csv_path = openface_processed + csv_name
#csv_path = '/home/chen/git-test/OpenFace-master/build/processed/webcam_2018-07-30-13-43.csv'
crop_image_txt_path = video_cores_file + 'crop_image_txt/'
if not os.path.exists(crop_image_txt_path):
    os.makedirs(crop_image_txt_path)

txt_path = crop_image_txt_path +'alldata.txt'
txt_f = open(txt_path, 'w')

video = cv2.VideoCapture(video_path)
WIDTH = video.get(3)
HEIGHT = video.get(4)
print('WIDTH,HEIGHT', WIDTH, HEIGHT)

with open(csv_path, 'r') as csv_f:
    reader = csv.reader(csv_f)
    rows = [row for row in reader]
#print(len(rows), len(rows[0]))
#print(type(rows[2][3]))   #都变成了str,用的时候需要注意了。
print(rows[0])
yaw_col_num = rows[0].index(' pose_Ry')
pitch_col_num = rows[0].index(' pose_Rx')
roll_coll_num = rows[0].index(' pose_Rz')
confidence_col_num = rows[0].index(' confidence')
success_col_num = rows[0].index(' success')
nosetip_x_col_num = rows[0].index(' x_33')
nosetip_y_col_num = rows[0].index(' y_33')
landmarks_name_x = [' x_0', ' x_1', ' x_2', ' x_3', ' x_4', ' x_5', ' x_6', ' x_7', ' x_8', ' x_9', ' x_10', ' x_11', ' x_12', ' x_13', ' x_14', ' x_15', ' x_16', ' x_17', ' x_18', ' x_19', ' x_20', ' x_21', ' x_22', ' x_23', ' x_24', ' x_25', ' x_26', ' x_27', ' x_28', ' x_29', ' x_30', ' x_31', ' x_32', ' x_33', ' x_34', ' x_35', ' x_36', ' x_37', ' x_38', ' x_39', ' x_40', ' x_41', ' x_42', ' x_43', ' x_44', ' x_45', ' x_46', ' x_47', ' x_48', ' x_49', ' x_50', ' x_51', ' x_52', ' x_53', ' x_54', ' x_55', ' x_56', ' x_57', ' x_58', ' x_59', ' x_60', ' x_61', ' x_62', ' x_63', ' x_64', ' x_65', ' x_66', ' x_67']
landmarks_name_y = [' y_0', ' y_1', ' y_2', ' y_3', ' y_4', ' y_5', ' y_6', ' y_7', ' y_8', ' y_9', ' y_10', ' y_11', ' y_12', ' y_13', ' y_14', ' y_15', ' y_16', ' y_17', ' y_18', ' y_19', ' y_20', ' y_21', ' y_22', ' y_23', ' y_24', ' y_25', ' y_26', ' y_27', ' y_28', ' y_29', ' y_30', ' y_31', ' y_32', ' y_33', ' y_34', ' y_35', ' y_36', ' y_37', ' y_38', ' y_39', ' y_40', ' y_41', ' y_42', ' y_43', ' y_44', ' y_45', ' y_46', ' y_47', ' y_48', ' y_49', ' y_50', ' y_51', ' y_52', ' y_53', ' y_54', ' y_55', ' y_56', ' y_57', ' y_58', ' y_59', ' y_60', ' y_61', ' y_62', ' y_63', ' y_64', ' y_65', ' y_66', ' y_67']
landmarks_col_num_x = [rows[0].index(xxx) for xxx in landmarks_name_x]
landmarks_col_num_y = [rows[0].index(yyy) for yyy in landmarks_name_y]
landmark_x1_num = rows[0].index(' x_1')
#landmark_y1_num = rows[0].index(' y_1')
landmark_x15_num = rows[0].index(' x_15')
#landmark_y15_num = rows[0].index(' y_15')

#print(yaw_col_num)

suc = True
while suc:
    suc, frame = video.read()
    if frame is not None:
        print(frame.shape)
        FRAME_NUM = int(video.get(1))    #帧数目是从1开始的。
        print('FRAME_NUM', FRAME_NUM)
        cut_size = 4.5 * max(abs(float(rows[FRAME_NUM][landmark_x1_num])-float(rows[FRAME_NUM][nosetip_x_col_num])), abs(float(rows[FRAME_NUM][landmark_x15_num]) - float(rows[FRAME_NUM][nosetip_x_col_num])))
        yaw = float(rows[FRAME_NUM][yaw_col_num])
        pitch = float(rows[FRAME_NUM][pitch_col_num])
        roll = float(rows[FRAME_NUM][roll_coll_num])
        nosetip_x = float(rows[FRAME_NUM][nosetip_x_col_num])
        nosetip_y = float(rows[FRAME_NUM][nosetip_y_col_num])
        confidence = float(rows[FRAME_NUM][confidence_col_num])
        success = float(rows[FRAME_NUM][success_col_num])
        if confidence > 0.5 and success == 1.0:
            if yaw < 30*(np.pi/180) and yaw > -30*(np.pi/180):
                box_ltop_x = nosetip_x - int(cut_size/2)
                box_ltop_y = nosetip_y - int(cut_size/2)
                box_rbottom_x = nosetip_x + int(cut_size/2)
                box_rbottom_y = nosetip_y + int(cut_size/2)
                if box_ltop_x < 0:
                    box_ltop_x = 0
                if box_ltop_y < 0:
                    box_ltop_y = 0
                if box_rbottom_x >= frame.shape[1]:
                    box_rbottom_x = frame.shape[1]
                if box_rbottom_y >= frame.shape[0]:
                    box_rbottom_y = frame.shape[0]
                cut_s = min(min(abs(box_ltop_y - nosetip_y),abs(nosetip_x - box_ltop_x)), min(abs(box_rbottom_x - nosetip_x), abs(box_rbottom_y - nosetip_y)))
                box_ltop_x = nosetip_x - cut_s
                box_ltop_y = nosetip_y - cut_s
                box_rbottom_x = nosetip_x + cut_s
                box_rbottom_y = nosetip_y + cut_s
                # if box_ltop_x < 0:
                #     box_ltop_x = 0
                #     box_rbottom_x = cut_size
                #     if cut_size > frame.shape[1]:
                #         box_rbottom_x = frame.shape[1]
                # if box_ltop_y < 0:
                #     box_ltop_y = 0
                #     box_rbottom_y = cut_size
                #     if cut_size > frame.shape[0]:
                #         box_rbottom_y = frame.shape[0]
                # if box_rbottom_x >= frame.shape[1]:
                #     box_rbottom_x = frame.shape[1]
                #     box_ltop_x = frame.shape[1] - cut_size
                #     if box_ltop_x < 0:
                #         box_ltop_x = 0
                # if box_rbottom_y >= frame.shape[0]:
                #     box_rbottom_y = frame.shape[0]
                #     box_ltop_y = frame.shape[0] - cut_size
                #     if box_ltop_y < 0:
                #         box_ltop_y = 0
                # cut_width = box_rbottom_x - box_ltop_x
                # cut_height = box_rbottom_y - box_ltop_y
                # diff = cut_height - cut_width
                # if diff >= 0:      #(cut_height大于等于cut_width)
                #     cut_size = cut_width
                #     if box_ltop_y == 0:
                #         box_rbottom_y = cut_size
                #     elif box_rbottom_y == frame.shape[0]:
                #         box_ltop_y = frame.shape[0] - cut_size
                # else:
                #     cut_size = cut_height
                #     if box_ltop_x == 0:
                #         box_rbottom_x = box_ltop_x + cut_size
                #     elif box_rbottom_x == frame.shape[1]:
                #         box_ltop_x = frame.shape[1] - cut_size
                frame = frame[int(box_ltop_y):int(box_rbottom_y), int(box_ltop_x):int(box_rbottom_x)]
                landmarks_x = [float(rows[FRAME_NUM][xxx]) - box_ltop_x for xxx in landmarks_col_num_x]
                landmarks_y = [float(rows[FRAME_NUM][yyy]) - box_ltop_y for yyy in landmarks_col_num_y]
                frame = cv2.resize(frame, (450, 450), interpolation=cv2.INTER_CUBIC)
                #print(landmarks_x)
                landmarks_x = [xxxx*450.0/(box_rbottom_x - box_ltop_x) for xxxx in landmarks_x]
                landmarks_y = [yyyy*450.0/(box_rbottom_y - box_ltop_y) for yyyy in landmarks_y]
                txt_f.write(str(FRAME_NUM)+'.jpg'+' '+ str(confidence) + ' ' +str(yaw)+' '+str(pitch)+' '+str(roll)+' '+' '.join([str(dd) for dd in landmarks_x])+' ' + ' '.join([str(dd) for dd in landmarks_y]) + '\n')
                cv2.imwrite(crop_image_txt_path + str(FRAME_NUM)+'.jpg', frame)





