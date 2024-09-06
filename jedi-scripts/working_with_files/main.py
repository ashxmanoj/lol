
# Open, read, and write to files

# file = open("my_file.txt")
# contents = file.read() # returns the contents of a file
# print(contents)
# file.close()

with open("my_file.txt", mode="a") as file: # with keyword manages the file directly
	# contents = file.read()
	file.write("Hello, World!!")

# If the file doesn't exist, python creates it from scratch

# Absolute file path always start off relative to the root or from the origin
# eg: /work/Project/talk.ppt

# Relative file path is relative to cwd
# eg : If we are inside Project folder, Project folder is our working directory
# eg: ./talk.ppt
# eg: ../report.doc if we want to move up