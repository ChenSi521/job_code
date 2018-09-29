#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib2 import Path
import pandas as pd

work_path = '/home/chen/datasets/movie/10030101/test1/01030010_flip_cut_aligned_Img/'
work_path1 = '/home/chen/datasets/movie/10030101/test1/01030010_flip_cut_aligned_Img_step/'
save_csv_name = 'Img_csv_concat6.csv'

work_path = Path(work_path)
csv_paths = work_path.glob('*.csv')
df0 = pd.read_csv('/home/chen/datasets/movie/10030101/test1/frame_det_00_000037.csv', header=0, sep=', ', index_col='face', engine='python')
print(df0)
df0 = df0.drop([0])
#df0 = pd.DataFrame([])
print(df0)
print(type(csv_paths))
#print(len(csv_paths))
i = 0
for csv_path in sorted(csv_paths):
    i +=1
    print(str(csv_path))
    df = pd.read_csv(str(csv_path), header=0, sep=', ', index_col='face', engine='python')
    #print(csv_path.name)
    df['frame_name'] = csv_path.name.split('.')[0]
    df0 = pd.concat([df0, df], axis=0, ignore_index=True, sort=True, join='outer')

print(str(work_path) + save_csv_name)
print(df0.shape)
df0.to_csv(work_path1 + save_csv_name, index_label='frame_num')
print(i)







