#!/usr/bin/env python
# _*_ coding:utf-8 -*-

#这是个很重要的发现，可以在b中添加元素，但是会自动添加在a中。
a = []
b = [1, 2]
c = [2, 3]

a.append(b)
a.append(c)

b.append(5)

print(a)

#下面这段代码证明，可以通过list()向外层List添加list。而且，可以用all_pics[0]进行引用。
#一个很有用的功能。
all_pics = []
list('tt')
#all_pics.append(list('tt'))  #用这种方式，在处理字符串时，会出错，会把字符串的每个字母转为列表的元素。
all_pics.append(['tt'])

print(all_pics)
print(all_pics[0])

a = [[1,2], [3,4]]
print([y for x in a for y in x])