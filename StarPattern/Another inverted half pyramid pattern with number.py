number = int(input("Enter the positive number: "))
for i in range(number, 0, -1):
    for j in range(0, i + 1):
        print(j, end=" ")
    print(" ")
