length = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(length - 1):
    for j in range(i, length):
        if a[i] > a[j]:
            res += 1
print(res)