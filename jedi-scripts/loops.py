fruits = ["Apple", "Peach", "Pear"]
# Loop through a list
# Loops allow us to execute the same line of code multiple times
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Range() generate a range of function to loop through
# print(range(1, 10)) #does not do anything all by itself
for number in range(0, 11, 2):
    print(number)

sum_of_num = 0
for i in range(1, 101):
    sum_of_num += i
print(sum_of_num)

# While Loops
# The loop that will continue going while the condition is True
something_is_true = True
while something_is_true:
    # Do something repeatedly
    print("Hello!")
