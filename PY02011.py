n = int(input())
a = list(map(int, input().split()))
ans = [float('inf'), -1]
for i in a:
    temp = sum([abs(i - x) for x in a])
    if temp < ans[0]:
        ans = [temp, i]
print(*ans)