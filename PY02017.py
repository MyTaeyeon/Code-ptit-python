for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    g = set()
    for i in a:
        if i in g:
            g.remove(i)
        else:
            g.add(i)
    print(*g)