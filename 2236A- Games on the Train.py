n = int(input())

ans = []

for _ in range(n):
    n = int(input())

    arr = list(map(int,input().split()))

    m = max(arr)-min(arr) + 1

    ans.append(m)

for i in ans:
    print(i)