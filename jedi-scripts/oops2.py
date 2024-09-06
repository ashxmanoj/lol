def function():
	pass


class User:

	def __init__(self, user_id, user_name):
		print("new user being created...")
		self.id = user_id
		self.username = user_name
		self.followers = 0  # pass on default value
		self.following = 0

	def follow(self, user):
		self.following = 1
		user.followers += 1


user_1 = User("001", "ash")
# How to create an attribute
# user_1.id = "001"
# user_1.username = "ash"
print(user_1.id)

user_2 = User("002", "jack")
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
# init function is invoked whenever we construct an object from a class.
# It's a general convention to use the name of the parameter to name of the attribute.

# Class Inheritance : The process of inheriting behavior and appearance from an existing class
class Animal:
	def __init__(self):
		self.num_eyes = 2

	def breathe(self):
		print("Inhale, exhale")


class Fish(Animal):
	def __init__(self):
		super().__init__()

	def breathe(self):
		super().breathe()
		print("doing this underwater")

	def swim(self):
		print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)