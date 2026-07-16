n = int(input())

ans = []

for _ in range(n):
    l = int(input())

    s = input()

    c = 0

    for i in range(1,l):
        if s[i]!=s[i-1]:
            c+=1

    if c==1:
        ans.append(2)

    else:
        ans.append(1)

for i in ans:
    print(i)