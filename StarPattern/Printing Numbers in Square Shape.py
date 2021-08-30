n = int(input("Enter the number of rows:"))
n_list = [[0 for x in range(n)] for y in range(n)]
m = 1
low = 0
high = n - 1
count = int(n + 1) // 2
for i in range(count):
    for j in range(low, high + 1):
        n_list[i][j] = m
        m += 1
    for j in range(low + 1, high + 1):
        n_list[j][high] = m
        m += 1
    for j in range(high - 1, low - 1, -1):
        n_list[high][j] = m
        m += 1
    for j in range(high - 1, low,  - 1):
        n_list[j][low] = m
        m += 1
    low += 1
    high -= 1

print(count)

for i in range(n):
    for j in range(n):
        print(n_list[i][j], end='\t')
    print()
