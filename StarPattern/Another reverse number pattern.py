number = int(input("Enter the positive number: "))
for i in range(number, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
        i = i - 1
    print(" ")
 