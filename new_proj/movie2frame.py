#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import cv2
from pathlib import Path
#import shutil

work_path = '/home/chen/datasets/Yawning/movie/'
work_path_P = Path(work_path)
work_path_save = '/home/chen/datasets/Yawning/frame/'
work_path_save_P = Path(work_path_save)


movies = work_path_P.rglob('*')
for num_movie, movie_path_P in enumerate(sorted(movies)):
    if movie_path_P.is_file():
        print num_movie, str(movie_path_P)
        video = cv2.VideoCapture(str(movie_path_P))
        suc = True
        i = 1
        #while i:
        while suc:
            suc, frame = video.read()
            if frame is not None:
                Frame_num = video.get(1)
                #print Frame_num
                frame_name = movie_path_P.stem +'_' + str(int(Frame_num)) + '.jpg'
                #print frame_name
                num_folder = int(Frame_num/5000)
                frame_path = work_path_save_P/movie_path_P.stem/str(num_folder)
                if not frame_path.exists():
                    frame_path.mkdir(parents=True)
                cv2.imwrite(str(frame_path/frame_name), frame)

                #print str(frame_path/frame_name)
                #i -=1
        #break



