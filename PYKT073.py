type = 3
ans = []
for _ in range(int(input())):
    g = input().split()
    if len(g) == 6:
        if type != -1:
            type = -1
            ans.append(1)
    elif len(g) == 7:
        type += 1
        if type % 4 == 0:
            ans.append(2)
print(len(ans), *ans, sep='\n')