t = int(input())
for z in range(t) :
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key = lambda x: x[1])
    s, k = 1, a[0][1]
    for i in range(1, n) :
        if a[i][0] >= k :
            s += 1
            k = a[i][1]
    print(s)
