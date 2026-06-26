n = int(input())

ans = []
for _ in range(n):  
    
    x = int(input())
    arr = list(map(int,input().split()))

    l,r = 0,1
    while r<x:
        if arr[r]>arr[l]:
            arr[r]=arr[l]
        l+=1
        r+=1

    ans.append(sum(arr))

for i in ans:
    print(i)