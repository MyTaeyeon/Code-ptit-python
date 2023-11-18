def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

for _ in range(int(input())):
    [n, k] = list(map(int, input().split()))
    a = []
    while len(a) < n:
        a += list(map(int, input().split()))

    ans = float('inf')
    for i in range(n):
        j = i + 1
        l = a[i]
        while l > k and j < n and j - i < ans:
            l = gcd(l, a[j])
            j+=1
        if l == k:
            ans = j - i
    print(ans if ans < float('inf') else -1) 