import turtle
p = turtle.Pen()
p.speed(0)

colors = ["red", "orange", "yellow", "green", "skyblue", "pink", "purple"]
fen = len(colors)
gen = 150 // fen
x = 0
for i in range(160):
    if i % gen == 0:
        if i // gen < len(colors):
            p.pencolor(colors[i // gen])
    p.forward(200)
    p.backward(250)
    p.forward(50)
    p.left(1)

turtle.done()
