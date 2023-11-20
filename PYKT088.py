n = int(input())
l = int(n ** (0.5))
a = [i for i in range(l + 1)]
for i in range(2, int(l**0.5) + 1):
    if a[i] == i:
        for j in range(i * i, l + 1, i): 
            if a[j] == j: 
                a[j] = i
ans = 0
for i in range(2, l + 1): 
    p = a[i]
    q = a[i // a[i]]
    if p * q == i and q != 1 and p != q: 
        ans += 1
    elif a[i] == i :
        if i ** 8 <= n: 
            ans += 1
print(ans)