#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import keyboard

while True:
    #try:
    if keyboard.is_pressed('a'):
        print('you pressed a key')
        break
    else:
        pass
    # except:
    #     #break
    #     print('except')
