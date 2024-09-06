

try:
	file = open("data.txt")
	a_dictionary = {"key": "value"}
	print(a_dictionary["ash"])
except FileNotFoundError:
	file = open("data.txt", "w")
	file.write("Something")
except KeyError as error_message:
	print(f"The Key {error_message} doesn't exist! ")
else:  # gets executed if there are no exceptions above
	contents = file.read()
	print(contents)
finally:  # gets executed no matter what
	# file.close()
	# print("File was closed")
	raise TypeError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
	raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)
