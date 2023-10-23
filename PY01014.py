[a, b, c] = list(map(int, input().split()))
ans = [str(x - a) for x in range((a + b) // b * b, c + 1, b)]
if len(ans) == 0:
    print(-1)
else:
    print(' '.join(ans))