n = int(input())

for _ in range(n):
    k = int(input())
    arr = []
    s = 0
    i = 1
    g = k
    while len(arr)<k:
        arr.append(g)
        g += g
        s += g
        i+=1

    if s>10**8:
        print("-1")
        continue

    print(*arr)