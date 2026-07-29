n = int(input())

ans = []

for _ in range(n):
    n,k = map(int,input().split())

    binary = list(input())

    for i in range(n - k):
        if binary[i] == '1':
            binary[i] = '0'
            if binary[i + k] == '0':
                binary[i + k] = '1'
            else:
                binary[i + k] = '0'
                
    if '1' in binary:
        ans.append("NO")    
    else:
        ans.append("YES")
    
for i in ans:
    print(i)