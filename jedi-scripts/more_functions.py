# Arguments with default values
from turtle import Turtle, Screen

from openai import models


# tim = Turtle()
# tim.write("May the force be with you!")
# In write method, text is required argument, whereas others are set to default values and are optional
# screen = Screen()
# screen.exitonclick()

def foo(a, b=4, c=6):
	print(a, b, c)


foo(4, 9)


# UNLIMITED POSITIONAL ARGUMENTS
def add(*args):  # we can pass any number of inputs
	# *(asterix) packs all the arguments into a tuple which is args
	print(args)  # prints out a tuple of all the inputs
	print(args[0])
	total = 0
	for n in args:
		total += n
	return total


print(add(3, 5, 7, 8))


# UNLIMITED KEYWORD ARGUMENTS
def calculate(n, **kwargs):
	# ** packs all the kw arguments into a dictionary
	print(kwargs)
	print(kwargs["add"])
	for key, value in kwargs.items():
		print(f"{key} -> {value}")
	n += kwargs["add"]
	n *= kwargs["multiply"]
	return n

print(calculate(2, add=3, multiply=5))

class Car:
	def __init__(self,**kwargs):
		self.make = kwargs["make"]
		# self.model = kwargs["model"]
		self.model = kwargs.get("model")
		self.colour = kwargs.get("color")
		self.seats = kwargs.get("seats")
	# .get() is better than dict[] coz if the key doesn't exist it returns None

car = Car(make="Nissan", model= "GT-R")
print(car.model)
print(car.seats)
