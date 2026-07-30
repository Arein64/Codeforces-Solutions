n, k = map(int,input().split())

arr = list(map(int,input().split()))

curr = 1

k%-len(arr)

while curr < k:
  curr += arr[curr - 1]

if curr == k:
    print("YES")
else:
    print("NO")
    