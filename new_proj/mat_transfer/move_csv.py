#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import shutil
from pathlib import Path
import pandas as pd

work_path = '/home/chen/datasets/movie_face_succ/'
work_path_P = Path(work_path)
work_path_save = '/home/chen/datasets/movie_face_right/'
work_path_save_P = Path(work_path_save)

csves = work_path_P.rglob('step_filter.csv')
i = 0
for num, csv in enumerate(sorted(csves)):

    csv_save = work_path_save_P/csv.parent.parent.name/csv.parent.name
    if not csv_save.exists():
        continue
    dt = pd.DataFrame([])
    df = pd.read_csv(str(csv), header=0, sep=',', engine='python')
    #print(str(csv.parent.parent))
    #print(str(csv_save))
    #shutil.copy(str(csv), str(csv_save))
    i += 1
    # (csv_save/csv.name).unlink()
    print(i)
    bmps_P = csv_save.glob('*.bmp')
    for num_bmp, bmp_path in enumerate(sorted(bmps_P)):
        txt_path = csv_save/(bmp_path.name.split('.')[0] + '.txt')
        f_txt = open(str(txt_path), 'w')
        ds = df[df.frame_name == bmp_path.name.split('.')[0]]
        dt = pd.concat([dt, ds], axis=0, ignore_index=True, sort=True, join='outer')
        f_txt.write(str(ds['pose_Rx'].tolist()[0]) + ' ' + str(ds['pose_Ry'].tolist()[0]) + ' ' + str(ds['pose_Rz'].tolist()[0]))
        f_txt.close()
    dt.to_csv(str(csv_save/'hand_filted.csv'), index_label='frame_num')

    #break


