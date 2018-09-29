#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import mxnet as mx
from mtcnn_detector import MtcnnDetector
import cv2
import os
from pathlib2 import Path
import shutil

detector = MtcnnDetector(model_folder='model', ctx=mx.cpu(0), num_worker = 4 , accurate_landmark = True)

j=0

fold_path = []
top_fold_path = Path('/home/chen/datasets/300W_LP')
#print(top_fold_path.iterdir())
for name_path in top_fold_path.iterdir():
    #print(name_path)
    #fold_path.append(str(top_fold_path)+"/"+str(name_path))
    fold_path.append(top_fold_path.joinpath(name_path))
print(fold_path)
for img_path in fold_path:
    img_name_list = sorted(img_path.glob('*.jpg'))
    for j in range(len(img_name_list)):   #zhe ge di fang xu yao jian 1 ma?
        img = cv2.imread(str(img_name_list[j]))
        mtcnn_face = detector.detect_face(img)

        if len(mtcnn_face[0])==1:
            total_boxes = mtcnn_face[0]
            #total_points = mtcnn_face[1]
            #i+=1
            #print('running i:',i)
            l_top_x = total_boxes[0][0]
            l_top_y = total_boxes[0][1]
            r_bottom_x = total_boxes[0][2]
            r_bottom_y = total_boxes[0][3]

            width = r_bottom_x - l_top_x
            height = r_bottom_y - l_top_y

            #de dao yi ge fan wei kuo da de box.
            l_top_x = l_top_x - 0.2*width
            l_top_y = l_top_y - 0.2*height
            r_bottom_x = r_bottom_x + 0.2*width
            r_bottom_y = r_bottom_y + 0.2*height

            num = 0
            mat_path = str(img_name_list[j]).split('.')[0] + '.mat'
            data = scio.loadmat(mat_path)
            for i in range(68):
                if data['pt2d'][0][i] < l_top_x or data['pt2d'][0][i] > r_bottom_x:
                    num += 1
                if data['pt2d'][1][i] < l_top_y or data['pt2d'][1][i] > r_bottom_y:
                    num += 1
            if num > 5:
                #cv2.rectangle()
                newpos1 = '/'.join(str(img_name_list[j]).split('/')[:-1]) + '/' + "mix_detected_face"
                if not os.path.exists(newpos1):
                    os.makedirs(newpos1)
                    # print(str(img_name_list[j]))
                    # print(newpos)
                shutil.move(str(img_name_list[j]), newpos1)
                mat_name = str(img_name_list[j]).split('.')[0] + "." + "mat"
                # print(mat_name)
                shutil.move(mat_name, newpos1)
                j +=1
                print("error img num:", j)









