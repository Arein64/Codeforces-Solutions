n = int(input())

ans = []

for _ in range(n):
    k = int(input())
    m = False
    arr = list(map(int,input().split()))
    p1,p2,p3 = False, False, False
    l=0
    c1,c2,c3 = 0,0,0
    while l<k:
        if arr[l]==1:
            c1+=1
        elif arr[l]==2:
            c2+=1
        elif arr[l]==3:
            c3+=1
        l+=1

        if c1 >= c2+c3:
            p1= True
            break
    
    c1,c2,c3 = 0,0,0
    while l<k:
        if arr[l]==1:
            c1+=1
        elif arr[l]==2:
            c2+=1
        elif arr[l]==3:
            c3+=1
        l+=1

        if c3 <= c1+c2:
            p2= True
            break
    
    if l<k:
        p3 = True
        
    if p1 and p2 and p3:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)