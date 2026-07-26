t = int(input())

ans = []

def check(sol,k):
    c = 0
    for i in range(len(sol)-1):
        if sol[i] == sol[i+1]:
            c+=1

    return c == k

for _ in range(t):
    n,k = map(int,input().split())

    def backtrack(sol,c0,c1):
        if len(sol)==n:
            if abs(c0-c1)>1:
                return -1    
            if check(sol,k):
                return sol
            return -1
        if len(sol)>n:
            return
        t1 = backtrack(sol+'0',c0+1,c1)
        if t1!=-1:
            return t1
        return backtrack(sol+'1',c0,c1+1)
    ch = backtrack("",0,0)
    
    ans.append(ch)


for i in ans:
    print(i)