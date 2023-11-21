def reduce(x):
    k = 0
    for i in str(x):
        k += ord(i) - 48
    return k

n = int(input())
ans = 1
n = reduce(n)
while n > 9:
    n = reduce(n)
    ans += 1
print(ans)