"""
Program : Q01 - Runner-Up Score

Topic : Lists

Problem Statement:
Store the participants' scores in a list and find the runner-up
(second highest unique) score.
"""

# Input scores
scores = [2, 3, 6, 6, 5]

# Remove duplicate scores
unique_scores = list(set(scores))

# Sort the list
unique_scores.sort()

# Display the runner-up score
print("Scores:", scores)
print("Runner-up score:", unique_scores[-2])