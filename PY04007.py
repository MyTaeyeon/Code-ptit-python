def mul(row, col, matrix):
    ans = 0
    for i in range(len(matrix[0])):
        ans += matrix[row][i] * matrix[col][i]
    return ans

for _ in range(int(input())):
    [m, n] = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        for j in range(m):
            print(mul(i, j, matrix), end=' ')
        print()