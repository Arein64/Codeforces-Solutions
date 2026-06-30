n = int(input())

ans = []

for _ in range(n):
    a,b = map(int,input().split())

    if a%b == 0:
        ans.append('YES')
    else:
        ans.append('NO')

for i in ans:
    print(i)