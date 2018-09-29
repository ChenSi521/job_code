#!/usr/bin/env python
# _*_ coding:utf-8 -*-

from pathlib import Path
import pandas as pd
import cv2
import numpy as np
import os
import time

work_path = '/home/chen/datasets/movie_face_supl/'
work_path_P = Path(work_path)

landmarks_name_x = ['x_0', 'x_1', 'x_2', 'x_3', 'x_4', 'x_5', 'x_6', 'x_7', 'x_8', 'x_9', 'x_10', 'x_11', 'x_12', 'x_13', 'x_14', 'x_15', 'x_16', 'x_17', 'x_18', 'x_19', 'x_20', 'x_21', 'x_22', 'x_23', 'x_24', 'x_25', 'x_26', 'x_27', 'x_28', 'x_29', 'x_30', 'x_31', 'x_32', 'x_33', 'x_34', 'x_35', 'x_36', 'x_37', 'x_38', 'x_39', 'x_40', 'x_41', 'x_42', 'x_43', 'x_44', 'x_45', 'x_46', 'x_47', 'x_48', 'x_49', 'x_50', 'x_51', 'x_52', 'x_53', 'x_54', 'x_55', 'x_56', 'x_57', 'x_58', 'x_59', 'x_60', 'x_61', 'x_62', 'x_63', 'x_64', 'x_65', 'x_66', 'x_67']
landmarks_name_y = ['y_0', 'y_1', 'y_2', 'y_3', 'y_4', 'y_5', 'y_6', 'y_7', 'y_8', 'y_9', 'y_10', 'y_11', 'y_12', 'y_13', 'y_14', 'y_15', 'y_16', 'y_17', 'y_18', 'y_19', 'y_20', 'y_21', 'y_22', 'y_23', 'y_24', 'y_25', 'y_26', 'y_27', 'y_28', 'y_29', 'y_30', 'y_31', 'y_32', 'y_33', 'y_34', 'y_35', 'y_36', 'y_37', 'y_38', 'y_39', 'y_40', 'y_41', 'y_42', 'y_43', 'y_44', 'y_45', 'y_46', 'y_47', 'y_48', 'y_49', 'y_50', 'y_51', 'y_52', 'y_53', 'y_54', 'y_55', 'y_56', 'y_57', 'y_58', 'y_59', 'y_60', 'y_61', 'y_62', 'y_63', 'y_64', 'y_65', 'y_66', 'y_67']
data_names = ['confidence', 'pose_Ry']

# bmp_paths = (work_path_P.rglob('*.bmp'))
chil_folders = [chil_folder for chil_folder in work_path_P.iterdir() if chil_folder.is_dir()]
chil_folders = [chil_folder for chil in chil_folders for chil_folder in chil.iterdir() if chil_folder.is_dir()]
#chil_folders = work_path_P.rglob('')
print(chil_folders)
#i = 0
for chil_folder in sorted(chil_folders):
    #break
    ds = pd.Series([])
    dt = pd.DataFrame([])
    dz = pd.DataFrame([])
    df05 = pd.DataFrame([])
    df10 = pd.DataFrame([])
    df15 = pd.DataFrame([])
    df20 = pd.DataFrame([])
    df25 = pd.DataFrame([])
    df30 = pd.DataFrame([])
    df_05 = pd.DataFrame([])
    df_10 = pd.DataFrame([])
    df_15 = pd.DataFrame([])
    df_20 = pd.DataFrame([])
    df_25 = pd.DataFrame([])
    df_30 = pd.DataFrame([])
    df_arr = [df05, df10, df15, df20, df25, df30, df_05, df_10, df_15, df_20, df_25, df_30]
    angle_paths = ['path05', 'path10', 'path15', 'path20', 'path25', 'path30', 'path_05', 'path_10', 'path_15',
                   'path_20', 'path_25', 'path_30']

    bmp_paths = (chil_folder.glob('*bmp'))
    for num, bmp_path in enumerate(sorted(bmp_paths)):
        sleep_secs = 0
        #i += 1
        framediff_bin = np.zeros((1, 1))
        if num == 0:
            pre_bmp_path = str(bmp_path)
            bmp_path_str = pre_bmp_path   #因为是第一张图片
            image0 = cv2.imread(pre_bmp_path)
            image_save = image0           #因为image0被用来标记landmarks，所以，这里就专门定义了一个image_save用来角度分类。
            if not os.path.exists(str(chil_folder) + '/frame_diff/'):
                os.makedirs(str(chil_folder) + '/frame_diff/')
            cv2.imwrite(str(chil_folder) + '/frame_diff/' + bmp_path.name, image0)
            #continue
        else:
            bmp_path_str = str(bmp_path)
            image0 = cv2.imread(bmp_path_str)
            image_save = image0
            image = image0[60:200, 60:200]
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image_gray = cv2.GaussianBlur(image_gray, (5, 5), 0)
            image_pre0 = cv2.imread(pre_bmp_path)
            image_pre = image_pre0[60:200, 60:200]
            image_pre_gray = cv2.cvtColor(image_pre, cv2.COLOR_BGR2GRAY)
            image_pre_gray = cv2.GaussianBlur(image_pre_gray, (5, 5), 0)

            framediff = cv2.absdiff(image_gray, image_pre_gray)
            framediff_bin = cv2.threshold(framediff, 35, 1, cv2.THRESH_BINARY)[1]

            pre_bmp_path = str(bmp_path)
        ds[num + 1] = np.sum(framediff_bin)
        if ds[num + 1] > 0.5 or num == 0:
            if not os.path.exists(str(bmp_path.parent) + '/frame_diff/'):
                os.makedirs(str(bmp_path.parent) + '/frame_diff/')
            cv2.imwrite(str(bmp_path.parent) + '/frame_diff/' + bmp_path.name, image_save)
            out_dir_str = str(bmp_path.parent) + '/Img_csv_txt'
            #print('hhhhhhhhhhhhhhh')
            shell_cmd = ["/home/chen/git-test/OpenFace-master/build/bin/FaceLandmarkImg -f ", bmp_path_str.replace('&', '\&'), " -2Dfp -pose -out_dir ", out_dir_str.replace('&', '\&')]
            #shell_cmd = ["/home/chen/git-test/OpenFace-master/build/bin/FaceLandmarkImg -f ", bmp_path_str, " -2Dfp -pose -out_dir ", out_dir_str]

            shell_cmd = ''.join(shell_cmd)
            #print(shell_cmd)
            txt_gotten = os.popen(shell_cmd)
                #'/home/chen/git-test/OpenFace-master/build/bin/FaceLandmarkImg -f ' + bmp_path_str + ' -2Dfp -pose -out_dir ' + out_dir_str)
            while os.path.exists(out_dir_str + '/' + bmp_path.name.split('.')[0] + '.csv') is False:
                time.sleep(1)
                sleep_secs += 1
                if sleep_secs >= 30:

                    break
                #pass
            #print('bbbbbbbbbbbbbbb')
            if sleep_secs >= 30:
                continue
            #print('tttttttttttttt')
            #print(out_dir_str + '/' + bmp_path.name.split('.')[0] + '.csv')
            df = pd.read_csv(out_dir_str + '/' + bmp_path.name.split('.')[0] + '.csv', header=0, sep=', ', engine='python')
            df['frame_name'] = bmp_path.name.split('.')[0]
            dz = pd.concat([dz, df], axis=0, ignore_index=True, sort=True, join='outer')
            df = df[(df['confidence'] > 0.95) & (df['pose_Ry'] <= 0.52) & (df['pose_Ry'] >= -0.52) & (
                        df['pose_Rx'] <= 0.45) & (df['pose_Rx'] >= -0.45)]
            if df.shape[0] > 0:
                if not os.path.exists(str(bmp_path.parent) + '/filted_without_dot/'):
                    os.makedirs(str(bmp_path.parent) + '/filted_without_dot/')
                cv2.imwrite(str(bmp_path.parent) + '/filted_without_dot/' + bmp_path.name, image_save)
                dt = pd.concat([dt, df], axis=0, ignore_index=True, sort=True, join='outer')
                ###================================================#
                landmarks_x = list(df.loc[0, landmarks_name_x])
                landmarks_y = list(df.loc[0, landmarks_name_y])
                data_others = list(df.loc[0, data_names])
                cv2.putText(image0,
                            str(int((bmp_path.name.split('_')[-1]).split('.')[0])) + '||' + str(data_others[0]) + '||' + str(data_others[1]),
                            (10, 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
                for i in range(68):
                    cv2.circle(image0, (int(landmarks_x[i]), int(landmarks_y[i])), 2, (0, 255, 0))
                #cv2.imshow('image_with_dot', image)
                if not os.path.exists(str(bmp_path.parent) + '/filted_with_dot/'):
                    os.makedirs(str(bmp_path.parent) + '/filted_with_dot/')
                cv2.imwrite(str(bmp_path.parent) + '/filted_with_dot/' + bmp_path.name, image0)
            if df.shape[0] > 0:
                for ang_num in range(6):
                    if np.pi*5*ang_num/180 <= df.loc[0, 'pose_Ry'] and df.loc[0, 'pose_Ry'] < np.pi*5*(ang_num +1)/180:
                        if not os.path.exists(str(bmp_path.parent) + '/angle_discr/' + angle_paths[ang_num]):
                            os.makedirs(str(bmp_path.parent) + '/angle_discr/' + angle_paths[ang_num])
                        #print(str(bmp_path.parent) + '/angle_discr/' + angle_paths[ang_num])
                        cv2.imwrite(str(bmp_path.parent) + '/angle_discr/' + angle_paths[ang_num] + '/' + bmp_path.name, image_save)
                        df_arr[ang_num] = pd.concat([df_arr[ang_num], df], axis=0, ignore_index=True, sort=True, join='outer')
                    if -np.pi*5*(ang_num + 1)/180 <= df.loc[0, 'pose_Ry'] and df.loc[0, 'pose_Ry'] < -np.pi*5*ang_num/180:
                        if not os.path.exists(str(bmp_path.parent) + '/angle_discr/' + angle_paths[6 + ang_num]):
                            os.makedirs(str(bmp_path.parent) + '/angle_discr/' + angle_paths[6 + ang_num])
                        #print(str(bmp_path.parent) + '/angle_discr/' + angle_paths[6 + ang_num])
                        cv2.imwrite(str(bmp_path.parent) + '/angle_discr/' + angle_paths[6 + ang_num] + '/' + bmp_path.name,
                                    image_save)
                        df_arr[6 + ang_num] = pd.concat([df_arr[6 + ang_num], df], axis=0, ignore_index=True, sort=True,
                                                    join='outer')
        if num % 100 == 0:
            print(time.asctime(time.localtime(time.time())), bmp_path_str)
    print(dt.shape, ds.shape, dz.shape)
    dt.to_csv(str(bmp_path.parent) + '/step_filter.csv')      #step之后的图片的csv
    ds.to_csv(str(bmp_path.parent) + '/diff_values.csv')      #两帧之间的差值
    dz.to_csv(str(bmp_path.parent) + '/frame_diffed.csv')     #满足帧间差过滤条件，剩余图片的csv
    for ang_num in range(12):
        if df_arr[ang_num].shape[0] != 0:
            df_arr[ang_num].to_csv(str(bmp_path.parent) + '/angle_discr/' + angle_paths[ang_num] + '.csv')
    # i +=1
    # # print(type(bmp_path))
    # bmp_path_str = str(bmp_path)
    # out_dir_str = str(bmp_path.parent)
    # # print(bmp_path_str, out_dir_str)
    # txt_gotten = os.popen(
    #     '/home/chen/git-test/OpenFace-master/build/bin/FaceLandmarkImg -f ' + bmp_path_str + ' -2Dfp -pose -out_dir ' + out_dir_str + '/csv_txt0')
    # if i % 100 == 0:
    #     i = 0
    #     print(time.asctime(time.localtime(time.time())), bmp_path_str)

    # for tt in txt_gotten.readlines():
    #     print(tt)
    #print(bmp_path)
    #break





