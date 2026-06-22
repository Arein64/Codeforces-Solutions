n = int(input())

ans = 0

for _ in range(n):
    s = 0
    arr = list(map(int,input().split()))
    for i in arr:
        s+=i
    if s>1:
        ans+=1

print(ans)