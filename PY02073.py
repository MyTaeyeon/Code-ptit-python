for _ in range(int(input())):
    n = int(input())
    x, y, z = list(map(int, input().split()))
    dp = [0]*(n+1)
    dp[1] = x
    for i in range(2, n+1):
        if i % 2 == 0:
            dp[i] = min(dp[i-1]+x, dp[i//2]+z)
        else:
            dp[i] = min(dp[i-1]+x, dp[i//2]+z+x, dp[(i+1)//2]+z+y)
    print(dp[n])
