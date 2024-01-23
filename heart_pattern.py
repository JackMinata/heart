# Heart Pattern in Python

# Function to print the heart pattern
def print_heart(size):
    for i in range(size//2, size, 2):
        for j in range(1, size-i, 2):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        for j in range(1, size-i+1):
            print(" ", end="")
        for j in range(1, i+1):
            print("*", end="")
        print()

    for i in range(size, 0, -1):
        for j in range(i, size):
            print(" ", end="")
        for j in range(1, (i*2)-1):
            print("*", end="")
        print()

# Size of the heart
size = 12

# Printing the heart pattern
print_heart(size)
