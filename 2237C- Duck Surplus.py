n = int(input())

ans = []

for _ in range(n):
    x = int(input())
    arr = list(map(int,input().split()))
    l,r= 0,1
    while r<x:
        if arr[l]>arr[r]:
            arr[l],arr[r]=arr[r],arr[l]+arr[r]

        l+=1
        r+=1
    ans.append(max(arr))


for i in ans:
    print(i)