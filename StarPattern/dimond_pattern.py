n = 5
for i in range(1, n+1):
    print('*'*(n+1-i)+' '*2*(i-1)+'*'*(n+1-i))
for i in range(1, n+1):
    print('*'*i+' '*2*(n-i)+'*'*i)