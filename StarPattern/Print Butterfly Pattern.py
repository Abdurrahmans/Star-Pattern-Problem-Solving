n = int(input("Enter the number of rows:"))
n = n//2
for i in range(1, n+1):
    for j in range(1, 2*n+1):
        if i < j < 2*n+1-i:
            print(' ', end=" ")
        else:
            print('*', end=" ")
    print()
for i in range(n, 0,-1):
    for j in range(2*n, 0, -1):
        if i < j < 2*n+1-i:
            print(' ', end=" ")
        else:
            print('*', end=" ")
    print()


