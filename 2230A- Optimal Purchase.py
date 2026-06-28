n = int(input())

prices = []

for _ in range(n):
    a,b,c = map(int,input().split())

    if b*3<c:
        prices.append(a*b)
        continue

    p=0
    if a>3:
        j = a//3
        p+= c*j
        a = a%3

    if a>0:
        p+= min(b*a,c)
    prices.append(p)

for i in prices:
    print(i)
