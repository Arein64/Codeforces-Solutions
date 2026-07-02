s = str(input())

vowels = ['A','E','I','O','U','Y']

ans = ''
for i in s:
    if i in vowels or i.upper() in vowels:
        continue
    m = i.lower()
    ans += '.' + m

print(ans)