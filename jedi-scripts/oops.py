# Procedural programming: We set up functions to do certain things, one procedure leads to another procedure
# Object-Oriented Programming (OOP) tries to model real-world objects

# Attributes are the variables that are associated with an object
# Methods are functions that are associated with an object
# Classes are blueprints, and individual objects generated from the blueprint are called instances
# Example: car = Car()  # PascalCase for class names, not CarBlueprint
# In Python, we use snake_case for variable and function names, and PascalCase for class names

from turtle import Turtle, Screen
from prettytable import PrettyTable

# Constructing/Initializing an object (instance) from the Turtle class
tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("Bisque4")
tim.forward(100)

# Accessing the attributes of an object
my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

# Accessing the methods of an object
# my_screen.exitonclick()

# Constructing an object (instance) from the PrettyTable class
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# Modifying attributes of the table object
print(table.align)
table.align = "l"  # Left-align the columns
print(table)
