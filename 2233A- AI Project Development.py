n = int(input())

an = []
for _ in range(n):
    a,b,c,d = map(int,input().split())

    ans = 0
    
    t1 = (a+b+c-1)//(b+c)

    t2 = d
    a-=b*d

    if a>0:
        c *=10
        t2 += (a+b+c-1)//(b+c)

    ans = min(t1,t2)
        
    an.append(ans)

for i in an:
    print(i)