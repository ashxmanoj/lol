# Data Types

# String
print("Hello"[4])
print("123" + "345")

# Integer
print(42)
print(342_654_389)

# Float
print(3.14159)

# Boolean 
print(True, False)

# Function is something like a machine in a factory, takes some input & returns some output
# print(len(546))
num_char = len(input("What is your name?"))
print(type(num_char))
new_num_char = str(num_char) 
print("Your name has " + new_num_char + " characters")

# Type casting or Type conversion
a = float(123)
print(type(a))

print(70 + float("100.5"))

# Mathematical Operations
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)  # outputs a floating point number
print(8 // 3)  # Floor division
print(2 ** 4)

# ()
# ** 
# * /
# + -
print(3 * 3 + 3 / 3 - 1) 
print(round(2.666666, 2))

score = 0
isWinning = True
# User scores a point
score += 10
print(score)
print(f"Your score is {score} and you are winning is {isWinning}")  # f-strings
# We can use f-strings to embed variables within strings
