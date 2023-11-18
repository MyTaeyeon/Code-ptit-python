mod = int(1e9) + 7
for _ in range(int(input())):
    a, b = list(map(int,input().split()))
    res = 0
    string = bin(b)
    string = string[2:][::-1]
    for i in range(len(string)):
        if string[i] == '1':
            res = (res + pow(a, i) % mod) % mod
    print(str(res))