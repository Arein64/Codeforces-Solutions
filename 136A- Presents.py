n = int(input())

gifts = list(map(int,input().split()))
ans = [1]*n

for i in range(n):
    ans[gifts[i]-1] = i+1

print(*ans)