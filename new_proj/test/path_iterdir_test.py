#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path

work_path = '/home/chen/datasets/movie_face/'

work_path_P = Path(work_path)

for path in work_path_P.iterdir():
    if path.is_dir():
        print(str(path))


# for path in work_path_P.glob(''):
#     if path.is_file():
#         print(str(path))
