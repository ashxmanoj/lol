# Depending on a conditition, we either do A or B
water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")
    
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    
    if age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >= 45 and age <= 55:
        print("Have a free ride on us!")
    else:
        print("Adult tickets are $12.")
        bill = 12
    
    take_photo = input("Do you want to have a photo take? Type y for Yes or n for No")
    if take_photo == 'y':
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Access denied")
    
# Comparision operators:  > < >= <= == !=
# Modulo operator %; returns remainder
# Logical operators : and/ or/ not
a = 12
print(a > 10 and a > 15)