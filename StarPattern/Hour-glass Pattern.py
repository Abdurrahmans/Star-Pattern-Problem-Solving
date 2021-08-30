n = int(input("Enter the number of rows:"))

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=" ")
    for k in range(2 * i+1):
        if k == 0 or k == 2 * i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n+1):
    for j in range(n - i):
        print(' ', end=" ")
    for k in range(2 * i+1):
        if k == 0 or i == n or k == 2 * i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
