# Local scope exists within functions
# When we create a variable or function within a function, it is only accessible inside that function.
# Similar to an apple tree within your fence

def drink_potion():
    potion_strength = 5
    print(potion_strength)


drink_potion()
# print(potion_strength)  # This would raise a NameError

# Global Scope
player_health = 10  # Available anywhere within our file

def drink_potion():
    print(player_health)


drink_potion()

# There is no Block Scope in Python!
game_level = 3
enemies = ["skeleton", "zombie", "alien"]
if game_level < 5:
    new_enemy = enemies[0]


print(new_enemy)  # Perfectly valid code unless 'new_enemy' is inside a function

# How to modify a global variable
enemies = 1


def increase_enemies():
    # global enemies  # Uncomment this line to modify the global variable
    enemies = 2  # We are actually creating a new local variable 'enemies' which is completely different from the global 'enemies'
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# It's a terrible idea to call your local variables and global variables with the same name.
# You can read a global variable and use it, but avoid modifying it within a function.

# Solution to the above problem

def increase_enemies(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside the function: {enemies}")

# Global constants
PI = 3.14159
URL = "https://www.udemy.com/course/100-days-of-code"