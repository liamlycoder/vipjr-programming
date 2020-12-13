import turtle as p
from random import randint

p.ht()
p.tracer(0)
p.setup(800, 600)
p.colormode(255)

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
food = {
    "x": 60,
    "y": 0
}
v = 300
r = randint(0, 255)
g = randint(0, 255)
b = randint(0, 255)
score = 0


def changeRight():
    global direction
    direction["x"] = 30
    direction["y"] = 0


def changeLeft():
    global direction
    direction["x"] = -30
    direction["y"] = 0


def changeUp():
    global direction
    direction["x"] = 0
    direction["y"] = 30


def changeDown():
    global direction
    direction["x"] = 0
    direction["y"] = -30


def draw(x, y, color):
    p.up()
    p.goto(x, y)
    p.dot(30, color)
    p.goto(280, 260)
    p.write("Score: {}".format(score), font=("Arial", 20, 'bold'))


def move():
    global snake, v, r, g, b, score
    p.clear()
    head = snake[-1].copy()
    head['x'] += direction["x"]
    head["y"] += direction["y"]
    snake.append(head)
    if food['x'] - 30 < snake[-1]['x'] < food['x'] + 30 and food['y'] - 30 < snake[-1]['y'] < food['y'] + 30:
        food['x'] = randint(-370, 370)
        food['y'] = randint(-270, 270)
        v -= 20
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        score += 1
    else:
        snake.pop(0)
    draw(food['x'], food['y'], "orange")
    for body in snake:
        draw(body["x"], body["y"], (r, g, b))
    if not check(snake[-1]['x'], snake[-1]['y']):
        p.clear()
        p.goto(-30, 30)
        p.write("游戏失败", font=("Arial", 30, "normal"))
        return
    p.ontimer(move, v)


def check(x, y):
    for s in snake[:-1]:
        if s['x'] - 15 < x < s['x'] + 15 and s['y'] - 15 < y < s['y'] + 15:
            return False
    return - 400 < x < 400 and -300 < y < 300


p.onkeypress(changeUp, "Up")
p.onkeypress(changeDown, "Down")
p.onkeypress(changeLeft, "Left")
p.onkeypress(changeRight, "Right")
move()
p.listen()
p.done()
