number = int(input("Enter the positive number: "))
for i in range(1, number + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print(" ")
