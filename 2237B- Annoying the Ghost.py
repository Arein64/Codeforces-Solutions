n = int(input())

ans = []

for _ in range(n):
    le = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    p = True
    swaps = 0

    for l in range(le):
        if a[l]<=b[l]:
            continue
        j = l+1
        found = False
        while j<le:
            if a[j]<=b[l]:
                found = True
                idx = j
                break
            j+=1
        if not found:
            ans.append(-1)
            p = False
            break
        else:
            for j in range(idx, l, -1):
                a[j], a[j - 1] = a[j - 1], a[j]
                swaps += 1  

    if p:
        ans.append(swaps)

for i in ans:
    print(i)