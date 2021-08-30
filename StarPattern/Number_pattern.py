number = int(input("Enter the positive number: "))
for i in range(number):
    for j in range(i):
        print(i, end=" ")
    print(" ")