import math
import itertools
n = int(input())
a = sorted(list(map(int, input().split())))
for k in list(itertools.combinations(a, 2)):
    if math.gcd(k[0], k[1]) == 1:
        print(k[0], k[1])
