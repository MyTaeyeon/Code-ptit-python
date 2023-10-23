for _ in range(int(input())):
    n = int(input())
    a = [list(map(float, input().split())) for _ in range(n)]
    dp = [1] * n
    for i in range(1, n):
        for j in range(0, i):
            if a[j][0] < a[i][0] and a[j][1] > a[i][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))