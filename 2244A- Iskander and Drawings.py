n = int(input())

ans = []
for _ in range(n):
    i = int(input())
    l = 0
    s = str(input())

    maximum,curr = 0,0

    while l<i:
        if s[l]=="*":
            maximum = max(maximum,curr)
            curr = 0
        else:
            curr+=1
            maximum = max(maximum,curr)
        l+=1

    if maximum%2==0:
        a = maximum//2
    else:
        a = maximum//2+1
    ans.append(a)

for i in ans:
    print(i)