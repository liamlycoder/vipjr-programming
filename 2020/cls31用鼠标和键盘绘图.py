# !/usr/bin/python
# coding: utf8
# Time: 2020/9/19 下午11:31
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle

p = turtle.Pen()


def up():
    p.sety(p.ycor() + 50)


def left():
    p.setx(p.xcor() - 50)


def right():
    p.setx(p.xcor() + 50)


def down():
    p.sety(p.ycor() - 50)


color_dic = {
    "green": (300, 140),
    "red": (300, 100),
    "blue": (300, 60)
}

eracer = {
    "white": (300, 0)
}

p1 = turtle.Pen()
p1.up()
p1.ht()
turtle.tracer(False)
for i in color_dic.keys():
    p1.goto(color_dic[i])
    p1.dot(30, i)
turtle.tracer(True)


def move(x, y):
    for color, pos in color_dic.items():
        if pos[0] + 15 > x > pos[0] - 15 and pos[1] + 15 > y > pos[1] - 15:
            p.pencolor(color)
            break
    else:
        p.setpos(x, y)


turtle.onkeypress(up, 'Up')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(down, 'Down')
turtle.onscreenclick(move)
turtle.listen()

turtle.done()
