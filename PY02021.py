for _ in range(int(input())):
    [m, n, k] = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    commons = []
    i = j = l = 0
    while i < m and j < n and l < k:
        if a[i] == b[j] == c[l]:
            commons.append(a[i])
            i += 1
            j += 1
            l += 1
        else:
            temp = max(a[i], b[j], c[l])
            if a[i] < temp:
                i += 1
            if b[j] < temp:
                j += 1
            if c[l] < temp:
                l += 1
    print(*commons) if len(commons) > 0 else print('NO')