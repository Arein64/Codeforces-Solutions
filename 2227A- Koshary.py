n = int(input())

ans = []

for _ in range(n):
    x,y = map(int,input().split())

    if x%2==1 and y%2==1:
        ans.append('NO')
    else:
        ans.append('YES')
for i in ans:
    print(i)