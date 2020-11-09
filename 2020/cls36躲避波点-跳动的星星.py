import turtle
import random

p = turtle.Pen()
p.up()
p.ht()
turtle.tracer(0)

stars = [
    [-300, 111],
    [-200, -109],
    [-100, 123],
    [0, 0],
    [100, 122],
    [200, 32],
    [300, -122]
]


def draw():
    for star in stars:
        p.goto(star[0], star[1])
        p.dot(40, "green")


def move():
    p.clear()
    for star in stars:
        star[1] -= 3
    draw()
    turtle.ontimer(move, 20)


count = 0


def tap(x, y):
    up_y = random.randint(100, 300)
    global count
    stars[count % len(stars)][1] += up_y
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




