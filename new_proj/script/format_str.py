#!/usr/bin/env python
# _*_ coding:utf-8 -*-

b = 'you'
a = '%20s' % b
print(a)

print(str(00001))

b = 'you'
a = '%20s' % b
print(a)

if len(b) < 5:
    b = '0'*(5-len(b)) + b
print(b)


p = ['1', '11', '2', '21', '111']
print(sorted(p))
#这个代码虽然简单，但是可以将‘数字字符串’按自然数的大小排列。
print(sorted(p, cmp=lambda x, y: len(x) - len(y)))

q = ['1.jpg', '11.jpg', '2.jpg', '21.jpg', '111.jpg']
print(sorted(q, cmp=lambda x, y: len(x) - len(y)))

u = ['/home/1.jpg', '/home/11.jpg', '/home/2.jpg', '/home/21.jpg', '/home/111.jpg', '/home/110.jpg', '/home/911.jpg']
print(sorted(u, cmp=lambda x, y: len(x) - len(y)))

for i in enumerate(sorted(u, cmp=lambda x, y: cmp(x, y))):
    print(i)


from pathlib import Path
dir = '/home/rr.jpg'
dir_P = Path(dir)
print(dir_P.name[:-4])