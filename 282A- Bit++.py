n = int(input())

x = 0
while n:
    s = str(input())
    if s[0] == '+' or s[-1] == '+':
        x+=1
    else:
        x-=1
    n-=1

print(x)