#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import pyautogui as pyag
import time
import cv2

print(pyag.position())
print(pyag.size())

img = cv2.imread('/home/chen/datasets/5222.jpg')
cv2.imshow('1', img)
while 1:
    if cv2.waitKey(1) & 0xFF == ord('0'):
        break
    if cv2.waitKey(1) & 0xFF == ord('8'):  #start
        print('输入了8')
        pyag.moveTo(1000, 500)
        pyag.click()
        while 1:
            if cv2.waitKey(1) & 0xFF == 40:  #ord('down'):  #向下
                pyag.press('down')
                time.sleep(0.5)
            if cv2.waitKey(1) & 0xFF == ord('e'): #end
                print('输入o成功')
                break
            if cv2.waitKey(1) & 0xFF == 38:  #ord('up'):  #向上
                pyag.press('down')
                time.sleep(0.5)

cv2.destroyAllWindows()

