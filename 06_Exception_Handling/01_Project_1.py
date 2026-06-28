try:
    filename = input("Enter the file name: ")

    with open(filename, "r") as file:
        lines = [line.strip() for line in file]

    purchased_items = 0
    free_items = 0
    amount = 0
    discount = 0

    section = 1

    for line in lines:

        if line == "":
            section += 1
            continue

        parts = line.split()

        if section == 1:
            purchased_items += 1
            amount += int(parts[-1])

        elif section == 2:
            free_items += 1

        elif section == 3:
            discount = int(parts[-1])

    print("No of items purchased:", purchased_items)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", amount - discount)

except FileNotFoundError:
    print("File not found.")

except ValueError:
    print("Invalid data in file.")

except Exception as e:
    print("Error:", e)