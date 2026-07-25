n = int(input())

notes = 0

if n>=100:
    notes += n//100
    n %= 100

if n>=20:
    notes += n//20
    n%=20

if n>=10:
    notes += n//10
    n %= 10

if n>=5:
    notes += n//5
    n%=5

if n>=1:
    notes+= n
    
print(notes)