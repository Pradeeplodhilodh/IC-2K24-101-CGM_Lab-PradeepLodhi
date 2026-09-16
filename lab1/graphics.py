import turtle

t = turtle.Turtle()
t.speed(3)

# 1. Straight Line
t.forward(200)

# 2. Circle
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(60)

# 3. Rectangle
t.penup()
t.goto(150, 100)
t.pendown()

for i in range(2):
    t.forward(150)
    t.right(90)
    t.forward(80)
    t.right(90)

# 4. Triangle
t.penup()
t.goto(-200, -100)
t.pendown()

for i in range(3):
    t.forward(120)
    t.left(120)

turtle.done()