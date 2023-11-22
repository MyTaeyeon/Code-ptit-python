while True:
    n = int(input())
    if n == 0: break
    a = [int(input()) for _ in range(n)]
    print(min(a), max(a)) if min(a) != max(a) else print('BANG NHAU')