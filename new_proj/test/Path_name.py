#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path

work_path = '/home/chen/datasets/movie_face_succ/Female_Mirror/01-FemaleNoGlasses-Normal_aligned/filted_with_dot'
work_path_P = Path(work_path)

print(work_path_P.name)
print(work_path_P.parent.name)
