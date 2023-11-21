for _ in range(int(input())):
    s = list(input())
    a = []
    sum = 0
    for i in s:
        if i.isdigit():
            sum += int(i)
        else:
            a.append(i)
    a.sort()
    print(*a, sum, sep='')