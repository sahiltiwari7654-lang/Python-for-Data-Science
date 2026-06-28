"""
Program : Project 1 - Happiness Calculator

Topic : Command Line Arguments

Problem Statement:
Increase happiness by 1 if a number is in the first list.
Decrease happiness by 1 if a number is in the second list.
Otherwise, happiness remains unchanged.
"""

# Input three strings
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
string3 = input("Enter third string: ")

# Convert into lists
like = string1.split("-")
dislike = string2.split("-")
numbers = string3.split("-")

happiness = 0

for num in numbers:
    if num in like:
        happiness += 1
    elif num in dislike:
        happiness -= 1

print("Final Happiness:", happiness)