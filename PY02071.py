mark = []
ans = []
def show(x):
    if x == 0:
        mark.sort(reverse=True)
        ans.append('('+' '.join(list(map(str, mark[1:])))+')')
    else:
        for i in range(x, 0, -1):
            if i <= mark[-1]:
                mark.append(i)
                show(x-i)
                mark.pop()

for _ in range(int(input())):
    n = int(input())
    mark = [float('inf')]
    ans = []
    show(n)
    print(len(ans))
    print(*ans)
