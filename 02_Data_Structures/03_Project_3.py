"""
Program : Q02 - Student Average Marks

Topic : Dictionaries

Problem Statement:
Store student names as keys and their marks as values (lists).
Ask the user to enter a student's name and display
the average percentage marks obtained by that student.
"""

# Dictionary containing student names and marks
students = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

# Take student name as input
name = input("Enter a name: ")

# Check if the student exists
if name in students:
    marks = students[name]
    average = sum(marks) / len(marks)
    print("Average percentage mark:", average)
else:
    print("Student not found.")