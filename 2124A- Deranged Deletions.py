n = int(input())

for _ in range(n):
    c = 0
    l = int(input())
    arr = list(map(int,input().split()))

    arr2 = sorted(arr)
    arr3 = []

    for i in range(l):
        if arr[i] == arr2[i]:
            c+=1
        else:
            arr3.append(arr[i])
    if c == l:
        print("NO")

    else:
        print("YES")
        print(len(arr3))
        print(*arr3)