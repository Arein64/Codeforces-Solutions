n = int(input())

for _ in range(n):
    a,b,x = list(map(int,input().split()))
    operations = 0

    while a!=b:
        if b>a and a - (b//x) < abs(a -b):
            b //= x
        elif a>b and b - (a//x) < abs(b-a):
            a //= x
        else:
            if a<b:
                a+=1
            else:
                b+=1
        operations+=1

    print(operations)