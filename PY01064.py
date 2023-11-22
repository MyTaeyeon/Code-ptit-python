def solve(n, k):
    if k == 2 ** (n - 1): return n
    if k > 2 ** (n - 1): return solve(n-1, k-2**(n-1))
    return solve(n-1, k)

for t in range(int(input())):
    n, k = list(map(int, input().split()))
    print(chr(solve(n, k) + ord('A') - 1))