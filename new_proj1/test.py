#!/usr/bin/env python
# _*_ coding:utf-8 -*-

import tensorflow as tf

a = tf.constant([1.0,2.0],name='a')
b = tf.constant([2.0,3.0],name='b')
c = tf.placeholder(tf.float32)
d = tf.convert_to_tensor(c)
result = a + d
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# print(b.eval(session = sess))
# f = b.eval(session = sess)
# #print(sess.run(result,feed_dict={c:[0.1,0.2]}))
# print(sess.run(result,feed_dict={c:f}))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(b.eval())
    f = b.eval(session = sess)
    f = sess.run(b)
    print(sess.run(result,feed_dict={c:f}))
