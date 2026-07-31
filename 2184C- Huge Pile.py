n = int(input())

ans = []

for _ in range(n):
    a,k = map(int,input().split())

    low, high = a,a
    d = 0
    c = True

    while high>=k:
        if k==low or k==high:
            c = False
            break
        low = low//2

        high = (high+1)//2
        d+=1
    if c:
        ans.append(-1)
    else:
        ans.append(d)
for i in ans:
    print(i)