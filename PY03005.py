import re, collections
n, k = list(map(int, input().split()))
words = []
for _ in range(n):
    line = input().lower()
    words += [word for word in re.split(r'[^\w]+', line) if word]
c = [[key, val] for key, val in collections.Counter(words).items() if val >= k]
c.sort(key=lambda x: (-x[1], x[0]))
for x in c:
    print(x[0], x[1])
