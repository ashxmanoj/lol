
# Every dictionary had two parts to it: Key & Value
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
}

# Retrieve an item from the dictionary
print(student_scores["Harry"])

# Add an item to the dictionary
student_scores["Neville"] = 60

# Edit an item in a dictionary
student_scores["Draco"] = 70

# Create an empty dictionary
empty_dict = {}

# Loop through a dictionary
for key in student_scores:
    print(key)
    print(student_scores[key])

# Nesting
travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille"]
    },
    "India": {
        "num_times_visited": 10,
        "cities_visited": ["Chennai", "Kolkata", "Hyderabad"]
    }
}

# Print chennai
print(travel_log["India"][2])
