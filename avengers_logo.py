import turtle

def draw_circle(av):
	# outer circle
	av.setposition(0, -280)
	av.pendown()
	av.begin_fill()
	av.color('red')
	av.pencolor('white')
	av.circle(300)
	av.end_fill()
	av.penup()

def draw_circle2(av):
	# inner circle
	av.pensize(2)
	av.setposition(0, -230)
	av.pendown()
	av.begin_fill()
	av.color('black')
	av.circle(250)
	av.end_fill()
	av.penup()

def draw_A(av):
	# drawing ‘A’
	av.setposition(30, -110)
	av.pendown()
	av.begin_fill()
	av.color('red')
	av.pensize(10)
	av.pencolor('white')
	av.forward(23)
	av.backward(123)
	av.left(60)
	av.backward(220)
	av.right(60)
	av.backward(100)
	av.right(117)
	av.backward(710)
	av.right(63)
	av.backward(110)
	av.right(90)
	av.backward(510)
	av.right(90)
	av.backward(100)
	av.right(90)
	av.backward(70)
	av.end_fill()
	av.penup()

def draw_triangle(av):
	# Triangle shape in ‘A’ to make it look like 2d
	av.pensize(10)
	av.setposition(53, -40)
	av.pendown()
	av.begin_fill()
	av.color('black')
	av.pencolor('white')
	av.right(90)
	av.forward(100)
	av.right(115)
	av.forward(250)
	av.right(157)
	av.forward(227)
	av.end_fill()

def draw_arrow(av):
	# arrow
	av.backward(80)
	av.left(42)
	av.forward(147)
	av.right(83)
	av.forward(140)

if __name__ == '__main__':
	win = turtle.Screen()
	win.bgcolor('black')

	avengers = turtle.Turtle()
	avengers.speed(10)
	avengers.pensize(10)
	avengers.penup()
	
	draw_circle(avengers)
	draw_circle2(avengers)
	draw_A(avengers)
	draw_triangle(avengers)
	draw_arrow(avengers)
	
	avengers.hideturtle()
	turtle.done()