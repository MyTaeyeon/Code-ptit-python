n = int(input())
ans = 0

comb = lambda x: 0 if x < 2 else x * (x - 1) // 2

rows = [0] * n
cols = [0] * n
for r in range(n):
    coins = input()
    for c in range(len(coins)):
        rows[r] += 1 if coins[c] == 'C' else 0
        cols[c] += 1 if coins[c] == 'C' else 0

for i in range(n):
    ans += comb(rows[i]) + comb(cols[i])

print(ans)