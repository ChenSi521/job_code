#!/usr/bin/env python
# _*_ coding:utf-8 -*-
import os

file_path = '/home/chen/datasets/movie/test/'
movie_names = os.listdir(file_path)
#print(movie_names)
movie_paths = [file_path + '/' + xx for xx in movie_names]
#print(movie_paths)
#txt_gotten = os.popen('/home/chen/git-test/OpenFace-master/build/bin/FeatureExtraction -verbose -f "/home/chen/datasets/movie/10030101/01030010_flip.MOV"')
for movie_path in movie_paths:
    txt_gotten = os.popen('/home/chen/git-test/OpenFace-master/build/bin/FeatureExtraction -2Dfp -pose -f ' + movie_path)
    for tt in txt_gotten.readlines():
        print(tt)
