#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path

work_path = '/home/chen/datasets/Smoke/Smoke_frame/all_frame/Smoke_movie/Continue smoking for fun and for you/Non-Smoking/'
work_path_P = Path(work_path)
if not work_path_P.exists():
    work_path_P.mkdir(parents=True)

