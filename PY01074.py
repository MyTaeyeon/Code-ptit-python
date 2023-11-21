import array, sys

MAX = 2000001
arr = array.array('i', [0] * MAX)
for i in range(2, int(MAX**0.5)):
    if arr[i] == 0:
        arr[i] = i
        for j in range(i * i, MAX, i):
            arr[j] = i

for i in range(4, MAX):
    arr[i] += arr[i // arr[i]] if arr[i] != 0 else i

res = 0
for _ in range(int(sys.stdin.readline())):
    res += arr[int(sys.stdin.readline())]
print(res)