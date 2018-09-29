#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import pyautogui as pyag
import time
import cv2

print(pyag.position())
print(pyag.size())

cv2.namedWindow('1')
cv2.moveWindow('1', 1500, 100)
img = cv2.imread('/home/chen/datasets/5222.jpg')
cv2.imshow('1', img)
pyag.moveTo(1600, 180)
while 1:
    # if cv2.waitKey(1) & 0xFF == ord('b'):
    #     break
    if cv2.waitKey(1) & 0xFF == ord('s'):  #start down
        print('输入了s')
        pyag.moveTo(1000, 500)
        pyag.click()
        pyag.moveTo(1600, 180)
        while 1:
            pyag.press('down')
            time.sleep(0.5)
            if cv2.waitKey(1) & 0xFF == ord('e'):  # end
                print('输入e成功')
                break
    if cv2.waitKey(1) & 0xFF == ord('w'):  # start up
        print('输入了w')
        pyag.moveTo(1000, 500)
        pyag.click()
        pyag.moveTo(1600, 180)
        while 1:
            pyag.press('up')
            time.sleep(0.5)
            if cv2.waitKey(1) & 0xFF == ord('e'):  # end
                print('输入e成功')
                break



            # key_value = cv2.waitKey(1)
            # print(key_value)
            # if key_value == -1:
            #     key_store = key_store
            # else:
            #     key_store = key_value
            # if key_store == 84:
            #     pyag.moveTo(1000, 500)
            #     pyag.click()
            #     while 1:
            #         pyag.press('down')
            #         time.sleep(0.5)
            #         if cv2.waitKey(1) & 0xFF == ord('e'):  # end
            #             print('输入9成功')
            #             break
            # if key_store == 82:
            #     pyag.moveTo(1000, 500)
            #     while 1:
            #         pyag.press('up')
            #         time.sleep(0.5)
            #         if cv2.waitKey(1) & 0xFF == ord('e'):  # end
            #             print('输入9成功')
            #             break
            # if key_store == ord('b'):
            #     break




            # if cv2.waitKey(1) & 0xFF == ord('e'): #end
            #     print('输入o成功')
            #     break
            # if cv2.waitKey(1) & 0xFF == 38:  #ord('up'):  #向上
            #     pyag.press('down')
            #     time.sleep(0.5)

cv2.destroyAllWindows()

