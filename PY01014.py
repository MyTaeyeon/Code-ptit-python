[a, b, c] = list(map(int, input().split()))
ans = [str(x - a) for x in range((a + b) // b * b, c + 1, b)]
print(-1) if len(ans) == 0 else print(' '.join(ans))