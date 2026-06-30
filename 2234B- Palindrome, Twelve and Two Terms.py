n = int(input())

ans = []

for _ in range(n):
    x = int(input())
    a,b = x,0

    while a>b:
        m = a
        while m>0:
            m=0
        a-=12
        b+=12
for i in ans:
    print(i)