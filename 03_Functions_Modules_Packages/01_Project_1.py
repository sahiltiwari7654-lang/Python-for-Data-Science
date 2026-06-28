"""
Program : Q01 - Sort Hyphen-Separated Colors

Topic : Functions

Problem Statement:
Write a Python function that accepts a hyphen-separated sequence
of colors as input and returns the colors in alphabetical order.
"""

def sort_colors(color_string):
    # Split the string into a list
    colors = color_string.split("-")

    # Sort the list alphabetically
    colors.sort()

    # Join the list back into a hyphen-separated string
    return "-".join(colors)


# Input from the user
color_input = input("Enter hyphen-separated colors: ")

# Display the result
print("Sorted colors:", sort_colors(color_input))