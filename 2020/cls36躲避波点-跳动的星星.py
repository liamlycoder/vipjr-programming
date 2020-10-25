# !/usr/bin/python
# coding: utf8
# Time: 2020/10/25 10:55
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import turtle
p = turtle.Pen()
p.penup()
p.hideturtle()
turtle.tracer(0)
stars = [
    [-200, 100],
    [-100, 43],
    [0, 210],
    [100, 99],
    [200, 194]
]

def draw():
    for star in stars:
        p.goto(star[0], star[1])
        p.dot(30, "green")

def move():
    p.clear()
    for star in stars:
        star[1] -= 5
    draw()
    turtle.ontimer(move, 100)


count = 0
def tap(x, y):
    up_y = 180
    global count
    stars[count % 5][1] += up_y
    count += 1


move()
turtle.onscreenclick(tap)
turtle.done()




