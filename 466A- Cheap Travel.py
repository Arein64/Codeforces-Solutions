n, r, p_one, p_many = map(int,input().split())

price = p_one * r

total = 0
if price<=p_many:
    print(n*p_one)

elif r>=n:
    print(min(p_one*n,p_many))

else:
    while n>=r:
        total+=p_many
        n-=r

    if n>0:
        if p_one<p_many:
            total += min(p_one*n,p_many)
        else:
            total += p_many
    
    print(total)