def isPrime(x):
    if x < 2: return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
prime_number = []
for i in range(len(a)):
    if isPrime(a[i]) == True:
        prime_number.append(a[i])
        a[i] = '?'
prime_number.sort()
p = 0
for i in range(len(a)):
    if a[i] == '?':
        a[i] = prime_number[p]
        p += 1
print(*a)