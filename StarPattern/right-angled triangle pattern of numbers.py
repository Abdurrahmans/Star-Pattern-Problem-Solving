number = int(input("Enter the positive number: "))
for i in range(1, number+1):
    for j in range(number, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(j, end=' ')
    print("")

