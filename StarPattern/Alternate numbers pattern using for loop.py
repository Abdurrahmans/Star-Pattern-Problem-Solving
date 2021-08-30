number = int(input("Enter the positive number: "))
for i in range(1, number + 1):
    for j in range(i):
        print(i*2-1, end=" ")
    print(" ")
