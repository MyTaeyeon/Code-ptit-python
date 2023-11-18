def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
n = int(input())
a = list(map(int, input().split()))
b = set()
c = [0]
for i in a:
    if i not in b:
        b.add(i)
        c.append(i)

left = [0] * (len(c))
for i in range(1, len(left)):
    left[i] = left[i - 1] + c[i]

ans = -1
for i in range(1, len(c)):
    if isPrime(left[i]) == True and isPrime(left[-1] - left[i]) == True:
        ans = i - 1
        break
print(ans) if ans != -1 else print('NOT FOUND')