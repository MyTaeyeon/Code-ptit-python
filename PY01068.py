import itertools

n, k = list(map(int, input().split()))
name = sorted(list(set(input().split())))

p = itertools.combinations(name, k)
[print(*x) for x in p]