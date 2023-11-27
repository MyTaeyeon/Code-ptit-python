test = int(input())
while test > 0:
    m, n, k = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(m)]
    prefixsum = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            prefixsum[i][j] = matrix[i-1][j-1] + prefixsum[i][j-1] + prefixsum[i-1][j] - prefixsum[i-1][j-1]
    
    for i in range(0, m-k+1):
        for j in range(0, n-k+1):
            print((prefixsum[i+k][j+k]-prefixsum[i+k][j]-prefixsum[i][j+k]+prefixsum[i][j])//(k**2), end=' ')
        print()
    test -= 1
