str = input()
if len(str) % 2 != 0: str = str[:-1]
arr = sorted(set(map(int, [str[i:i+2] for i in range(0, len(str),2)])))
print(*arr)