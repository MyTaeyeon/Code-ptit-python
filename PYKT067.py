import itertools
tests = int(input())
while tests > 0:
    tests -= 1
    n = list(range(1, int(input())+1))
    permutations = list(itertools.permutations(n))
    print(len(permutations))
    [print(''.join(map(str, x)), end=' ') for x in permutations[::-1]]
    print()
