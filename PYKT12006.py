[n, k] = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sorted([a[i] - b[i] for i in range(len(a))])
while k < len(c) and c[k] < 0:
    k += 1
print(sum(b) + sum(c[:k]))