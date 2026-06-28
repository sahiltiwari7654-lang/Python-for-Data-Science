"""
Module : name_utils

Contains functions to:
1. Check whether a name is a palindrome.
2. Count the vowels in a name.
3. Find the frequency of each letter.
"""

def ispalindrome(name):
    # Remove spaces and convert to lowercase
    text = name.replace(" ", "").lower()

    if text == text[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")


def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in name:
        if ch in vowels:
            count += 1

    print("No of vowels:", count)


def frequency_of_letters(name):
    frequency = {}

    for ch in name:
        if ch != " ":
            frequency[ch] = frequency.get(ch, 0) + 1

    print("Frequency of letters:", end=" ")

    first = True
    for key, value in frequency.items():
        if not first:
            print(", ", end="")
        print(f"{key}-{value}", end="")
        first = False

    print()