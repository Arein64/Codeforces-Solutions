n = int(input())

ans = []

for _ in range(n):
    total_time = 0
    s1 = input()
    s2 = input()

    l1 = len(s1)
    l2 = len(s2)
    l = 0

    while l<l1 and l<l2 and s1[l] == s2[l]:
        l+=1
        if l == l1 or l == l2:
            break
    
    if l>0:
        total_time+=1
    
    total_time += l + l1-l + l2-l
    
    ans.append(total_time)
for i in ans:
    print(i)