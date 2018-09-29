#!/usr/bin/env python
# _*_ coding:utf-8 -*-
import os


work_path = '/home/chen/datasets/movie/10030101/'
viedo_name = '01030010_flip_cut.avi'

viedo_path = work_path + viedo_name
corresp_output = work_path + viedo_name.split('.')[0] + '/'
if not os.path.exists(corresp_output):
    os.makedirs(corresp_output)
openface_processed = corresp_output + 'openface_processed/'
if not os.path.exists(openface_processed):
    os.makedirs(openface_processed)
txt_gotten = os.popen('/home/chen/git-test/OpenFace-master/build/bin/FeatureExtraction -verbose -f ' + viedo_path + ' -out_dir ' + openface_processed )
#txt_gotten = os.popen('/home/chen/git-test/OpenFace-master/build/bin/FeatureExtraction -2Dfp -pose -f "/home/chen/datasets/viedo/10030101/01030010_flip_cut.MOV"')
for tt in txt_gotten.readlines():
    print(tt)
#print(txt_gotten)