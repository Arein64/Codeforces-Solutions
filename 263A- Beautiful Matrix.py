arr = []
for i in range(5):
    a = list(map(int,input().split()))
    arr.append(a)

l = len(arr)
i = len(arr[0])
x,y = -1,-1
for n in range(l):
    for m in range(i):
        if arr[n][m]==1:
            x,y = n,m

steps = 0

x_diff = abs(2-x)
y_diff = abs(2-y)

print(x_diff+y_diff)