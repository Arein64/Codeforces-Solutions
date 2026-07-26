n = int(input())

ans = []

def calc(i,length,arr):
    new_arr = [0]*length
    for j in range(1,length-1):
        if arr[j]<i:
            new_arr[j-1] += arr[j]
        elif arr[j]>i:
            new_arr[j+1] += arr[j]
        
    return new_arr[1:length-1] == arr

for _ in range(n):
    length = int(input())
    length+=2
    c = True

    weights = list(map(int,input().split()))

    arr = [0]*length

    for i in range(1,length-1):
        arr[i]=weights[i-1]

    present = set(arr)
    mini = min(arr)
    maxi = max(arr)

    for i in range(mini,maxi):
        if i in present:
            continue
        else:
            a = calc(i,length,arr)
            if a:
                c = False
                ans.append("YES")
                break
    
    if c:
        ans.append("NO")

for i in ans:
    print(i)