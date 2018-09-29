#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import cv2

video_name = '01150012_flip.MOV'
video_path = '/home/chen/datasets/movie/10030101/' + video_name
#cam_path = '/home/chen/datasets/movie/10030101/webcam_2018-07-25-15-17.avi'
#cam = cv2.VideoCapture(cam_path)
video = cv2.VideoCapture(video_path)
out_video = '/home/chen/datasets/movie/10030101/' + video_name.split('.')[0] + '_cut.' + 'avi'
print(out_video)
FPS = video.get(5)
print(FPS)
FOURCC = video.get(6)
#FOURCC = cv2.VideoWriter_fourcc(*'XVID')
WIDTH = video.get(3)
HEIGHT = video.get(4)
print(WIDTH, HEIGHT, int(WIDTH - HEIGHT))
videowriter = cv2.VideoWriter(out_video, int(FOURCC), int(FPS), (int(HEIGHT+350), int(HEIGHT)))
#videowriter = cv2.VideoWriter(out_video, int(FOURCC), int(FPS), (int(WIDTH), int(HEIGHT)))

suc = True
while suc:
    suc, frame = video.read()
    if frame is not None:
        FRAME_NUM = video.get(1)
        print('frame_num', FRAME_NUM)
        frame = frame[0:int(HEIGHT), int(WIDTH - HEIGHT-350):int(WIDTH)]
        cv2.waitKey(1)
        videowriter.write(frame)

video.release()
#cam.release()
videowriter.release()
cv2.destroyAllWindows()





