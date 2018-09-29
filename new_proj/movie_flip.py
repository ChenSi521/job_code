#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import cv2
import os

work_path = '/home/chen/datasets/movie/01/10030112/'
# video_names = ['22510001.MOV']
video_names = os.listdir(work_path)

for video_name in video_names:
    video_path = work_path + video_name
    if os.path.isfile(video_path) is True:
        print(video_path)
        flip_out_path = work_path + 'flip_video2/'
        if not os.path.exists(flip_out_path):
            os.makedirs(flip_out_path)
        out_movie = flip_out_path + video_name.split('.')[0] + '_flip.MOV'

        cam = cv2.VideoCapture(video_path)
        print('fps:', cam.get(5))
        WIDTH = cam.get(3)
        HEIGHT = cam.get(4)
        print('WIDTH, HEIGHT', WIDTH, HEIGHT)
        FPS = cam.get(5)
        FOURCC = cam.get(6)
        print(FOURCC)
        FRAME_COUNT = cam.get(7)
        print("FRAME_COUNT", FRAME_COUNT)
        videowriter = cv2.VideoWriter(out_movie, int(FOURCC), int(FPS), (int(WIDTH), int(HEIGHT)))
        success = True
        #frame_num = 0
        while success:
            success, frame = cam.read()
            if frame is not None:
                #frame_num += 1
                FRAME_NUM = cam.get(1)
                print('frame_num', FRAME_NUM)
                frame = cv2.flip(frame, -1)
                videowriter.write(frame)

        cam.release()
        videowriter.release()
        #cv2.destroyAllWindows()











