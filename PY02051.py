n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
a = [0] * n
curr = matrix[n - 2][-1]
for i in range(n - 3, -1, -1):
    a[i] = (sum([x for x in matrix[i][i + 1:]]) - curr) // (n-i-1)
    curr += a[i]
a[-2], a[-1] = matrix[0][-2] - a[0], matrix[0][-1] - a[0]
print(*a)
