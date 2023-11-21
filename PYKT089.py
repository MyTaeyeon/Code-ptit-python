n = int(input())
a = list(map(int, input().split()))
while len(a) < n:
    a += list(map(int, input().split()))
even = sorted([i for i in a if i % 2 == 0])
odd = sorted([i for i in a if i % 2 == 1], reverse=True)

i, j = 0, 0
for x in a:
    if x % 2 == 0:
        print(even[i], end=' ')
        i += 1
    else:
        print(odd[j], end=' ')
        j += 1
print()