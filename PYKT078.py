for _ in range(int(input())):
    [n, m] = list(map(int, input().split()))
    negative = []
    positive = []
    a = list(map(int, input().split()))
    r = a.index(max(a))
    a = a[:r] + [m] + a[r:]
    for i in a:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    print(*negative, end=' ')
    print(*positive)