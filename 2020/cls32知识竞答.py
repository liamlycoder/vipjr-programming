# !/usr/bin/python
# coding: utf8
# Time: 2020/10/11 00:41
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import time
import turtle

questionList = []
answerList = []
optionList = []
positionList = []
questionIndex = 0
questionPen = turtle.Pen()
resultPen = turtle.Pen()
def init():
    global questionList, answerList, optionList, \
        positionList, questionIndex, questionPen, resultPen
    # turtle.bgpic("")
    turtle.setup(720, 720)
    questionList = [
        '整数在Python中用什么表示？',
        "怎样在Python中输出？",
        "条件判断在Python中是怎么写的？"
    ]
    answerList = ['int', 'print', 'if']
    optionList = [
        ['A.int', 'B.float', 'C.str'],
        ['A.while', 'B.print', 'C.input'],
        ['A.if', 'B.list', 'C.turtle']
    ]
    positionList = [
        [-180, -100],
        [0, -100],
        [200, -100]
    ]
    questionIndex = 0
    questionPen.ht()
    resultPen.ht()
    resultPen.penup()
    resultPen.goto(-100, -50)

# 绘制文字
def drawText(p, color, text, size=40):
    p.pencolor(color)
    p.write(text, font=('Arial', size))

# 按序显示题目和选项
def getQuestion(p, index):
    p.clear()
    p.penup()
    p.goto(-300, 150)
    if index >= len(questionList):
        p.goto(-50, 0)
        drawText(p, 'green', '已通关')
        return
    drawText(p, 'black', questionList[index])

    for i in range(3):
        p.penup()
        p.goto(positionList[i][0] - 55, positionList[i][1] + 25)
        drawText(p, 'black', optionList[index][i])

def checkPos(x, y):
    global questionIndex, resultPen
    for i in range(len(optionList)):
        if positionList[i][0] - 80 < x < positionList[i][0] + 30 \
                and positionList[i][1] < y < positionList[i][1] + 80:
            if optionList[questionIndex][i].split('.')[1] == answerList[questionIndex]:
                questionIndex += 1
                result(resultPen, 'right')
                getQuestion(questionPen, questionIndex)
            else:
                result(resultPen, 'wrong')

def result(p, r):
    p.goto(-100, 100)
    if r == 'right':
        drawText(p, 'green', '恭喜你回答正确', 30)
    else:
        drawText(p, 'red', '再想想哦', 30)
    time.sleep(1)
    p.clear()


init()
getQuestion(questionPen, questionIndex)
turtle.tracer(0)
turtle.onscreenclick(checkPos)
turtle.done()


