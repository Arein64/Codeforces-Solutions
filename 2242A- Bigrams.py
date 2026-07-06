n = int(input())

ans = []

for _ in range(n):
    check = False
    m = False 
    k = int(input())
    cards = list(map(int,input().split()))
    if k==1:
        if cards[0]>2:
            m = True
    else:
        for i in cards:
            if i==1:
                continue
            if i  >= 3:
                m = True
                break
            if i%2==1:
                i-=1
            elif i%2 == 0 and not check:
                check = True
            elif i%2 == 0 and check:
                m = True
                break
        
    if m:
        ans.append("YES")
    
    else:
        ans.append("NO")
for i in ans:
    print(i)