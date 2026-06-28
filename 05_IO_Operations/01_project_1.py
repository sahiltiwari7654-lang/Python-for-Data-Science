from collections import Counter

# Enter the file name
filename = input("Enter file name: ")

# Open the file
with open(filename, "r") as file:
    lines = file.readlines()

# -----------------------------
# Find Meeting Time
# -----------------------------
line_count = len(lines)

if line_count == 12:
    time = "12 PM"
elif line_count > 12:
    time = f"{line_count - 12} PM"
else:
    time = f"{line_count} AM"

# -----------------------------
# Find Meeting Place
# -----------------------------
words = []

for line in lines:
    line = line.replace(",", "")
    line = line.replace(".", "")
    line = line.lower()
    words.extend(line.split())

frequency = Counter(words)

place = max(frequency, key=frequency.get)

# -----------------------------
# Output
# -----------------------------
print("Meeting time:", time)
print("Meeting place:", place.capitalize(), "Street")