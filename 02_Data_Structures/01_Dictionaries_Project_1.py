"""
Program : Q01 - People and Interesting Facts

Topic : Dictionaries

Problem Statement:
Create a dictionary containing people's names and one interesting fact
about each person. Display all the facts, update one fact, add a new
person, and display the updated dictionary.
"""

# Create a dictionary
people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display original dictionary
print("Original Dictionary:\n")

for name, fact in people.items():
    print(f"{name}: {fact}")

# Change one fact
people["Jeff"] = "Is afraid of heights."

# Add a new person
people["Jill"] = "Can hula dance."

# Display updated dictionary
print("\nUpdated Dictionary:\n")

for name, fact in people.items():
    print(f"{name}: {fact}")