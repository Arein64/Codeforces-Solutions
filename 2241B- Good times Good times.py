n = int(input())

int_max = 10**9

ans = []
         
for _ in range(n):
    x = int(input())
    l = len(str(x))
    y = 10**l + 1
    ans.append(y)

for i in ans:
    print(i)