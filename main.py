print("NUMERIC DIAMOND PATTERN")
size = int(input("Enter pattern size (1 to 9): "))

if size < 1 or size > 9:
    print("Please enter a size from 1 to 9.")
else:
    for row in range(1, size + 1):
        for space in range(size - row):
            print(" ", end="")
        for number in range(1, row + 1):
            print(number, end="")
        for number in range(row - 1, 0, -1):
            print(number, end="")
        print()

    for row in range(size - 1, 0, -1):
        for space in range(size - row):
            print(" ", end="")
        for number in range(1, row + 1):
            print(number, end="")
        for number in range(row - 1, 0, -1):
            print(number, end="")
        print()
