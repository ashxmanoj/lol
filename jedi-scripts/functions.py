# Functions give us a way of referring to all those instructions to program "karel" the robot at the same time.
# def my_function():  # function definition
#     print("Hello")
#     print("Bye")
#
#
# my_function()  # calling the function

# Function with inputs
def greet(name):
    print(f"Hello {name}")
    print("May the force be with you!")


# Argument is the actual piece of data that's gng to be passed over to this function
# Parameter is the name of the data
greet("Ash")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


# Positional Arguments
greet_with("Ash", "Delhi")

# Keyword Arguments
greet_with(name="Jack", location="Nowhere")

# Functions are some sort of machines which take some input & after some processing it returns output


def format_name(f_name, l_name):
    """Takes first and last name and format it to return the title case version of the string."""
    if f_name == "" or l_name == "":
        return "Invalid input"
    name = f"{f_name.title()} {l_name.title()}"
    return name  # returns tell the computer that it's the end of function & now exit the function


print(format_name('arthur', 'dent'))

# Docstrings are used to create little bits of documentation to explain the function
"""
Hi! I'm a multi-line comment
Author: Ash
Course: 100DaysOfCode
Avoid using multi-line comments.
"""
