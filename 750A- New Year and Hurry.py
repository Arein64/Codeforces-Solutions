problems, time = map(int,input().split())

current = 20*60

midnight = 24*60

remaining = midnight - time

solved = 0
if remaining<=current:
    print(0)
else:
    t = 5
    remaining-=5
    if remaining>=current:
        solved+=1
    while remaining>current:
        solved+=1
        if solved>problems:
            solved-=1
            break
        t = 5*solved
        remaining-=t
        if remaining<current:
            solved-=1
            break

    print(solved)