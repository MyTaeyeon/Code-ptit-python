s1 = set(map(lambda x: x.lower(), input().split()))
s2 = set(map(lambda x: x.lower(), input().split()))

union = sorted(list(s1.union(s2)))
insect = sorted(list(s1.intersection(s2)))

print(*union)
print(*insect)