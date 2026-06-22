n,k = map(int,input().split())

arr = list(map(int,input().split()))

k-=1

y = arr[k]

c = 0

for i in arr:
    if i>=y and i>0:
        c+=1
    else:
        break
print(c)