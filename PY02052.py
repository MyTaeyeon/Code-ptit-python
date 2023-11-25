n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
half_right = sum([sum(matrix[i][:i]) for i in range(1, n)])
half_left = sum([sum(matrix[i][1-(n - i):]) for i in range(0, n - 1)])
print('YES') if abs(half_left - half_right) <= k else print('NO')
print(abs(half_left - half_right))
