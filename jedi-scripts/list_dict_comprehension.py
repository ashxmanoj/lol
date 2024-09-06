import pandas as pd
from reportlab.lib.pagesizes import letter
from torch.utils.hipify.hipify_python import value
import random

# List Comprehension allows us to create new list from existing list
numbers = [1, 2, 3]
# new_list = []
#
# for num in number:
# 	new_list.append(num + 1)
# print(new_list)

# new_list = [new_item for item in list]
new_list = [num + 1 for num in numbers]
print(new_list)

name = "Arthur Dent"
letter_list = [letter for letter in name]
print(letter_list)

# Python sequences : strings/ lists/ range/ tuple
range_list = [2*i for i in range(1, 5)]
print(range_list)

# Conditional list comprehension
# new_list = [new_item for item in list if test]
names = ["Ash", "Alex", "Marvin", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)

# Dictionary Comprehension allows us to create a new dictionary based on values in existing dictionary
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.item() if test}
random_scores = {key:random.randint(1, 100) for key in names}
print(random_scores)

passed_students = {key:value for (key, value) in random_scores.items() if value >= 60}
print(passed_students)

test_str = "geeks for geeks"
test_list = test_str.split(" ")
print(test_list)

student_dict = {
	"student" : ["Harry", "Ron", "Hermione"],
	"scores" : [80, 67, 94]
}
data = pd.DataFrame(student_dict)
print(data)
# Loop through rows of a dataframe
for (index, row) in data.iterrows():
	print(row.student)

