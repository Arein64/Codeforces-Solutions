n = int(input())

int_max = 10**9

ans = []

def good_numbercheck(n):
    return True if len(set(str(n)))<=2 else False
         
for _ in range(n):
    x = int(input())
    ch = False
    arr = []
    for j in range(2,int_max):
        if good_numbercheck(j) and good_numbercheck(j*x):
            ans.append(j)
            break

for i in ans:
    print(i)