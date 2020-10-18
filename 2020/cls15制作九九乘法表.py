# !/usr/bin/python
# coding: utf8
# Time: 2020/10/11 19:08
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm

"""九九乘法表"""
for row in range(1, 10):
    first = 1
    while first <= row:
        s = "{}x{}={}".format(first, row, first*row)
        print(s, end='\t')
        first += 1
    print()

"""方形螺旋图"""
"""
import turtle
p = turtle.Pen()
p.speed(0)
p.pencolor('red')
p.pensize(3)
for i in range(50):
    p.fd(30 + i*10)
    p.left(92)
turtle.done()
"""

"""螺旋红圆点"""
import turtle
b = turtle.Pen()
b.pencolor('red')
b.pensize(4)
b.speed(0)
for i in range(30):
    b.penup()
    b.fd(50+i*10)
    b.pendown()
    b.dot(1+i*2)
    b.left(95)
turtle.done()


turtle.done()






