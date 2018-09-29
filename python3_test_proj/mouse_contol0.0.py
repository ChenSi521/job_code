#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import pyautogui as pyag
import time
import cv2

print(pyag.position())
print(pyag.size())

while 1:
    img = cv2.imread('/home/chen/datasets/5222.jpg')
    cv2.imshow('1', img)
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break
    if cv2.waitKey(1) & 0xFF == ord('8'):  #start
        print('输入了8')
        pyag.moveTo(1000, 500)
        while 1:
            pyag.scroll(-2)
            time.sleep(0.5)
            if cv2.waitKey(1) & 0xFF == ord('9'): #end
                print('输入9成功')
                break
cv2.destroyAllWindows()
# while True:
#     num = input('退出')
#     if num == str([0]):
#         break


