import turtle
import random

star_x = 0
star_y = 0
p = turtle.Pen()
p.up()
turtle.tracer(0)
turtle.setup(720, 720)
balls = [
    [470, 199],
    [470, -199]
]
frequency = 0


def draw():
    p.goto(star_x, star_y)
    p.down()
    p.color("red", "red")
    p.begin_fill()
    for i in range(5):
        p.fd(50)
        p.lt(144)
    p.end_fill()
    p.penup()
    for pos in balls:
        p.goto(pos[0], pos[1])
        p.dot(30)


def move():
    p.clear()
    global star_y
    star_y -= 5
    global frequency
    for pos in balls:
        if abs(pos[0] - star_x) < 40 and abs(pos[1] - star_y) < 40 \
                or not inside(star_x, star_y):
            turtle.write("游戏失败", font=("Arial", 20, "bold"))
            return
        pos[0] -= 3
    if frequency % 100 == 0:
        ball_x, ball_y = 470, random.randint(-470, 470)
        balls.append([ball_x, ball_y])
    frequency += 1
    draw()

    turtle.ontimer(move, 20)


def tap(x, y):
    global star_y
    up_y = 180
    star_y += up_y


def inside(x, y):
    return -360 < x < 360 and -360 < y < 360


move()
turtle.onscreenclick(tap)
turtle.done()
