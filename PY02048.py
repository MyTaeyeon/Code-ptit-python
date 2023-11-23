n, k = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
res = 1
for i in range(1, n):
    if a[i] - a[i - 1] > k: res += 1
print(res)
