height = 7

for row in range(height):
    for col in range(height * 2 - 1):
        if ((col == 0 or col == height * 2 - 2) or (row == col) or (col == height * 2 - 2 - row)):
            print("*", end="")
        else:
            print(" ", end="")
    print()