#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import numpy as np
import scipy.io as scio
import os
# matFile 写入
save_matFile = 'save_matlabdata.mat'
save_matlabdata = np.array([1,2,3,4,5])
scio.savemat(save_matFile, {'array':save_matlabdata, 'array':save_matlabdata})
#会自动转为(1,5)。可能是mat格式的数据决定的吧，最低2维。
print(save_matlabdata.shape)

3
a = [1.0, 2.0, 3.0]
a = [xxx*4/2*2 - 1 for xxx in a]
print(a)

print(os.getcwd())
