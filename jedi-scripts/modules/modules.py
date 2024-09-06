# We are going to use the random module to create randomness in our programs.
# Python uses the Mersenne Twister algorithm to generate pseudo-random numbers.
import random
import my_module

# As our code becomes complex, we split it up into individual modules.
# Different modules have different functions, similar to workers focusing on different components in a car factory.
print(my_module.my_favorite_number)

# Generate a random integer between a and b (inclusive)
random_integer = random.randint(1, 10)
print(random_integer)

# Generate a random floating-point number between 0 and 1
random_number = random.random() * 10
print(random_number)

# Generate a random floating-point number between a and b (inclusive).
random_float = random.uniform(1, 10)
print(random_float)