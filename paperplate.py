import turtle
pen = turtle.Turtle()
pen.speed(10)

for i in range(180):
    pen.forward(100)
    pen.right(30)
    pen.forward(20)
    pen.left(60)
    pen.forward(50)
    pen.right(30)

    pen.penup()
    pen.setposition(0,0)

    pen.pendown()
    pen.right(2)

turtle.done()

    
