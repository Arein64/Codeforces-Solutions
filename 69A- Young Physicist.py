n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

hmp = {
    'x': 0,
    'y': 0,
    'z':0
}

m = arr[0]

for i in range(len(arr)):
    for j in range(len(m)):
        if j==0:
            hmp['x'] += arr[i][j]
        elif j==1:
            hmp['y'] += arr[i][j]
        else:
            hmp['z'] += arr[i][j]

ans = True

for keys,values in hmp.items():
    if values!=0:
        ans = False

if ans:
    print("YES")
else:
    print("NO")