import math
key = '0123456789ABCDEF'
with open('DATA.in') as file:
    t = int(file.readline())
    for _ in range(t):
        b = int(math.log2(int(file.readline())))
        num = file.readline().rstrip('\n')
        while len(num) % b != 0: num = '0' + num
        print(''.join([key[int(num[i:i+b], 2)] for i in range(0, len(num), b)]))