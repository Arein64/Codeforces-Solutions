n = int(input())

ans = []

for _ in range(n):
    w = 0
    l,c = map(int,input().split())

    a1 = list(map(int,input().split()))
    a2 = list(map(int,input().split()))
    ch = True
    m = 0

    for i in range(l):
        if a1[i]>=a2[i]:
            w = a1[i]-a2[i]
            m+=w
        else:
            ch = False
            break
    if ch:
        ans.append(m)
    else:
        ch = True
        a1.sort()
        a2.sort()
        m = 0
        m+=c
        for i in range(l):
            if a1[i]>=a2[i]:
                w = a1[i]-a2[i]
                m+=w
            else:
                ch = False
                break
        if ch:
            ans.append(m)
        else:
            ans.append(-1)
for i in ans:
    print(i)