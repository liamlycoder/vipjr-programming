# !/usr/bin/python
# coding: utf8
# Time: 2020/10/18 10:45
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import random
import turtle

s = turtle.Screen()
s.setup(1000, 1000)
turtle.tracer(0)
balls = [
    [470, 199],
    [470, -199]
]
p = turtle.Pen()
frequency = 0


def draw():
    p.clear()
    p.penup()
    for pos in balls:
        p.goto(pos[0], pos[1])
        p.dot(30)


def move():
    global frequency
    for pos in balls:
        pos[0] -= 3
    if frequency % 100 == 0:
        ball_x, ball_y = 470, random.randint(-470, 470)
        balls.append([ball_x, ball_y])
    frequency += 1

    draw()
    turtle.ontimer(move, 1)


move()
turtle.done()
