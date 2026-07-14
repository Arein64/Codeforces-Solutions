n = int(input())

ans = []

for _ in range(n):
    c = True
    r = int(input())
    arr = list(map(int,input().split()))
    su = 0
    s = 0
    for i in range(r):
        su += i+1
        s += arr[i]
        if s>=su:
            continue
        else:
            c = False
            ans.append("NO")
            break
    if c:
        ans.append("YES")

for i in ans:
    print(i)