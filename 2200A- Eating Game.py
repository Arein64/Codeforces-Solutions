n = int(input())

ans = []

for _ in range(n):
    p = int(input())
    arr = list(map(int,input().split()))

    k = 0
    a = 0

    for i in range(p):
        if arr[i]>k:
            k = arr[i]
            a = 1
        elif arr[i]==k:
            a+=1
    ans.append(a)
for i in ans:
    print(i)