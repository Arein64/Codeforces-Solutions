s = str(input())

msg = 'hello'

i = 0

for j in s:
    if i == 5:
        break
    if j == msg[i]:
        i+=1
    else:
        continue

if i == 5:
    print('YES')

else:
    print('NO')