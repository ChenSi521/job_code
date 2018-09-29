#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib2 import Path

work_path = "/home/chen/datasets/movie_face_backup/movie_face、"
work_path_P = Path(work_path)
work_path1 = '/home/chen/datasets/movie_face_500/Female/'
work_path_P1 = Path(work_path1)

#folders = work_path_P.rglob('frame_det_00_000001.bmp')
#for num, folder in enumerate(sorted(folders)):
for i in range(1, 44):
    newfolder_name = work_path_P1/('%02d' % i)     #产生以0填充。
    if not newfolder_name.exists():    ##############
        newfolder_name.mkdir(parents=True)
