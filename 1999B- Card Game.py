n = int(input())

for _ in range(n):
    a,b,c,d = map(int,input().split())

    if a>c and a>d and b>c and b>d:
        print("4")
                    
    elif ((a>c and b>=d) or (a>=c and b>d)) and ((a>d and b>=c) or (a>=d and b>c)):
        print("4")

    elif ((a>c and b>=d) or (a>=c and b>d) or (a>d and b>=c) or (a>=d and b>c)):
        print("2")

    else:
        print("0")