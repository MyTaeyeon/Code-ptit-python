for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int,input().split())))
    print( (arr[-1] - arr[0] + 1) - len(set(arr)) )
    