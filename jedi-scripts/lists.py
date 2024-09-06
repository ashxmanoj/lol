# Lists are a fundamental data structure in Python.
# Data structures are ways of storing and organizing data efficiently.

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits)
print(fruits[0])  # Access the first item (index 0)
print(fruits[-1])  # Access the last item (negative indexing)
print(len(fruits))  # Get the length of the list

# Lists are mutable, meaning we can change their contents
fruits[2] = "Avocado"
print(fruits)

# Add an item to the end of the list using the append() method
fruits.append("Banana")
print(fruits)

# Attempting to access an index that doesn't exist will raise an IndexError
# print(fruits[10])  # This would raise an IndexError

# For more information on Python data structures:
# https://docs.python.org/3/tutorial/datastructures.html

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# Nested lists: Create a list containing other lists
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
