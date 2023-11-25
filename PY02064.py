for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = [0] + list(map(int, input().split()))
    dp = [[0]*(n+1) for _ in range(5*k+1)]
    key = [5, 1, -2, 3, -4]
    for i in range(1, 5*k+1):
        dp[i][i] = dp[i-1][i-1] + a[i]*key[i%5]
        for j in range(i+1, n-5*k+i+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]+a[j]*key[i%5])
    print(dp[-1][-1])
