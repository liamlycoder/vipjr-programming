import turtle as p

p.ht()
p.tracer(0)

p.ht()
snake = [
    {"x": 10, "y": 0},
    {"x": 10, "y": 30},
    {"x": 10, "y": 60},
]
direction = {
    "x": 0,
    "y": 30
}


def changeRight():
    direction["x"] = 30
    direction["y"] = 0


def changeLeft():
    direction["x"] = -30
    direction["y"] = 0


def changeUp():
    direction["x"] = 0
    direction["y"] = 30


def changeDown():
    direction["x"] = 0
    direction["y"] = -30


def draw(x, y, color):
    p.up()
    p.goto(x, y)
    p.dot(30, color)


def move():
    p.clear()
    head = snake[-1].copy()
    head['x'] += direction["x"]
    head["y"] += direction["y"]
    snake.append(head)
    snake.pop(0)
    for body in snake:
        draw(body["x"], body["y"], "red")
    p.ontimer(move, 200)


def start(x, y):
    move()


p.onkeypress(changeUp, "Up")
p.onkeypress(changeDown, "Down")
p.onkeypress(changeLeft, "Left")
p.onkeypress(changeRight, "Right")
p.onscreenclick(start)
p.listen()
p.done()
