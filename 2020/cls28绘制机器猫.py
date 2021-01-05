import turtle

p = turtle.Pen()


def face():
    p.fillcolor("blue")
    p.begin_fill()
    p.circle(100)
    p.end_fill()
    p.fillcolor("white")
    p.begin_fill()
    p.circle(80)
    p.end_fill()


def eye():
    p.penup()
    p.fillcolor("white")
    for i in [-1, 1]:
        p.goto(20 * i, 140)
        p.pendown()
        p.begin_fill()
        p.circle(20)
        p.end_fill()
        p.penup()
        p.goto(10 * i, 160)
        p.pendown()
        p.dot(10)
        p.penup()


def nose():
    p.penup()
    p.goto(0, 120)
    p.pendown()
    p.fillcolor("red")
    p.begin_fill()
    p.circle(12, 360, 30)
    p.end_fill()
    p.penup()


def mouth():
    p.pendown()
    p.right(90)
    p.forward(90)
    p.left(90)
    p.circle(110, -40)
    p.circle(110, 80)
    p.right(40)


def beard():
    p.left(40)
    for i in [1, -1]:
        for r in range(3):
            p.penup()
            p.goto(15 * i, 110 - r * 10)
            if not (i == -1 and r == 0):
                p.right(20 * i)
            p.pendown()
            p.forward(50 * i)


face()
eye()
nose()
mouth()
beard()

p.hideturtle()
turtle.done()
