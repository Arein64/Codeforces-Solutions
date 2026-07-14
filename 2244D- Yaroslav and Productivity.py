n = int(input())

ans = []

for _ in range(n):
    m,j = map(int,input().split())

    m_arr = list(map(int,input().split()))
    j_arr = list(map(int,input().split()))

    s = sum(m_arr)

    for i in j_arr:
        for j in range(i):
            m_arr[j] = -m_arr[j]
        su = sum(m_arr)
        s = max(s,su)
    ans.append(s)

for i in ans:
    print(i)