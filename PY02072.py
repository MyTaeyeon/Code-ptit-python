n = int(input())
a = list(map(int, input().split()))
ans, cnt, res = 0, 0, max(a)
for i in range(len(a)):
    if a[i] == res: cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)
