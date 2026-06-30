n = int(input())

for _ in range(n):
    a,b,c,d = map(int,input().split())

    hrs = 0
    while a>0:        
        hrs+=1
        a-=b
        
        
    print(hrs)