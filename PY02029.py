m, n = list(map(int, input().split()))
a = list(map(int, input().split()))
scores = [0] * (n + 1)
for i in a: scores[i] += 1
first = max(scores)
second = 0
ans = 0
for i in range(1, n + 1):
    if scores[i] > second and scores[i] < first:
        second = scores[i]
        ans = i
print(ans) if ans != 0 else print('NONE')
