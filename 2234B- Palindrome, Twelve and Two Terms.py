n = int(input())

for _ in range(n):
    ch = False
    x = int(input())
    a = x%12
    b = x-a
    if a == 10:
        if x == 10:
            print(-1)
        else:
            print(22,x-22)
    else:
        print(a,b)