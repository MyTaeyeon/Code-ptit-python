tests = int(input())
import math
while tests > 0:
    tests -= 1
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(len(a) - 1):
        if a[i] > a[i+1]*2:
            while a[i] > a[i+1]*2:
                a[i] = math.ceil(a[i]/2)
                ans += 1
        elif a[i] < math.ceil(a[i+1]/2):
            while a[i] < math.ceil(a[i+1]/2):
                a[i] *= 2
                ans += 1
    print(ans)
