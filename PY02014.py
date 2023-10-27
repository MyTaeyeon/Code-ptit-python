import bisect
def isPrime(x):
    for i in range(2, int(x**0.5 + 1)):
        if x % i == 0:
            return False
    return True
primes = [0]
for i in range(2, 10010):
    if isPrime(i) == True:
        primes.append(i)
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in a:
    l = bisect.bisect_left(primes, i)
    ans = max(ans, min(i - primes[l - 1], primes[l] - i))
print(ans)