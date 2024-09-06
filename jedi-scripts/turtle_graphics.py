import turtle
from turtle import Turtle, Screen
import random
# from turtle import *
# import turtle as t
screen = Screen()
screen.bgcolor("black")
screen.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("cornflower blue")

# Draw a square
# for i in range(4):
# 	tim.forward(100)
# 	tim.right(90)

# Draw a dashed line
# for i in range(15):
# 	tim.forward(10)
# 	tim.pendown()
# 	tim.forward(10)
# 	tim.penup()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Draw different shapes
# for n in range(3, 10):
# 	tim.pencolor(random.choice(colours))
# 	for i in range(n):
# 		tim.forward(100)
# 		tim.right(360 / n)


def random_color():
	r_hex = random.randint(0, 255)
	g_hex = random.randint(0, 255)
	b_hex = random.randint(0, 255)
	colours = (r_hex, g_hex, b_hex)
	return colours

# Generate a random walk
# tim.pensize(10)
# random_angle = [0, 90, 180, 270]
# for i in range(100):
# 	tim.setheading(random_color())
# 	tim.forward(30)
# 	tim.pencolor(colours)


# Generate a spirograph
neon_palette = [(116, 0, 184), (105, 48, 195), (94, 96, 206), (83, 144, 217), (78, 168, 222), (72, 191, 227), (86, 207, 225),
				(100, 223, 223), (114, 239, 221), (128, 255, 219)]

tim.speed("fastest")
for _ in range(round(360 / 5)):
	tim.circle(100)
	tim.setheading(tim.heading() + 5)
	tim.pencolor(random.choice(neon_palette))


screen.exitonclick()
