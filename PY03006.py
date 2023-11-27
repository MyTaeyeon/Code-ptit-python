import re, collections
n = int(input())
words = []
for _ in range(n):
    line = input().lower()
    cleaned_text = re.sub(r'\d', '', line).lower()
    words += [word for word in re.split(r'[^\w]+', cleaned_text) if word]
c = [[key, val] for key, val in collections.Counter(words).items()]
c.sort(key=lambda x: (-x[1], x[0]))
for x in c:
    print(x[0], x[1])
