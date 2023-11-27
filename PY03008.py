n = int(input())
points = [0] * (n+1)
for _ in range(n-1):
    u, v = list(map(int, input().split()))
    points[u] += 1
    points[v] += 1
ans = False
for i in points:
    if i == n - 1:
        ans = True
        break
print('Yes') if ans else print('No')
