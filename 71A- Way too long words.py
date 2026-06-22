n = int(input())

ans = []

while n>0:
    s = str(input())
    if len(s)>10:
        n-=1
        word = s[0]+str(len(s)-2)+s[-1]
        ans.append(word)
        continue
    ans.append(s)
    n-=1

for i in ans:
    print(i)