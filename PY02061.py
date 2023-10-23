for _ in range(int(input())):
    [rows, cols] = list(map(int, input().split()))
    m = 3
    a = [list(map(int, input().split())) for _ in range(rows)]
    b = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(0, rows - m + 1):
        for j in range(0, cols - m + 1):
            for row in range(i, i + m):
                for col in range(j, j + m):
                    ans += a[row][col] * b[row - i][col - j]
    print(ans)
