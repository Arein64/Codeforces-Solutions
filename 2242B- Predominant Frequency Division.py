n=int(input())

ans=[]
for _ in range(n):
    k=int(input())
    arr=list(map(int,input().split()))
    c1,c2= 0,0
    mn=float('inf')
    ok=False

    for i in range(k-1):
        if arr[i]==1:
            c1+=1
        else:
            c1-=1

        if arr[i]==3:
            c2-=1
        else:
            c2+=1

        if c2>=mn:
            ok=True
            break

        if c1>=0:
            mn=min(mn,c2)

    if ok:
        ans.append("YES")
    else:
        ans.append("NO")

for i in ans:
    print(i)