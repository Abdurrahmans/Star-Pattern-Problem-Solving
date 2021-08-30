n = int(input("Enter the number of rows:"))
for i in range(1, 2 * n):
    for j in range(1, 2 * n):
        if j == n or i == j or i + j == 2 * n:
            print("*", end="  ")
        else:
            print(' ', end="  ")
    print()
