n, l = map(int,input().split())

names = []

for _ in range(n):
    name = input()
    names.append(name)

if l==0:
    names.sort()
    print(len(names))
    for name in names:
        print(name)

else:
    arr = []
    for _ in range(l):
        arr.append(input().split())

    maxi = []
    res = []

    def bt(le,curr):
        global maxi
        if le == n:
            check = False
            for i in range(len(curr)):
                for j in range(i + 1, len(curr)):
                    pair1 = [curr[i], curr[j]]
                    pair2 = [curr[j], curr[i]]
                    if pair1 in arr or pair2 in arr:
                        check = True
                        break
                if check:
                    break
            if not check:
                m = len(maxi)
                t = len(curr)
                if t>m:
                    maxi = curr[:]

            return

        bt(le+1,curr)

        curr.append(names[le])
        bt(le+1,curr)
        curr.pop()
        
    bt(0,[])

    print(len(maxi))

    maxi.sort()

    for name in maxi:
        print(name)