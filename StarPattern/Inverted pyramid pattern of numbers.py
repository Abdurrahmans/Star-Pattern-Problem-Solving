number = int(input("Enter the positive number: "))
for i in range(1, number+1):
    for j in range(number):
        print(i, end=" ")
    print(" ")
    number = number - 1
