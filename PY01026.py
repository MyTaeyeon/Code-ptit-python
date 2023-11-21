import collections

for i in range(int(input())):
    a = collections.Counter(list(input()))
    b = collections.Counter(list(input()))
    print(f"Test {i + 1}: YES") if a == b else print(f"Test {i + 1}: NO")
