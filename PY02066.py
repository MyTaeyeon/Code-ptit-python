n = int(input())
a = [0]
while len(a) <= n:
    a = a + list(map(int, input().split()))
a.sort()
[print(''.join(list(map(lambda x: str(x) + '\n', range(a[i - 1] + 1, a[i])))), sep='', end='') for i in range(1, len(a))]
if a[-1] == n:
    print('Excellent!')

