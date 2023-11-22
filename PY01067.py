def decimalToTernary(decimal_number):
    result = ''
    while decimal_number > 0:
        decimal_number, remainder = divmod(decimal_number, 3)
        result = str(remainder) + result
    return result

for _ in range(int(input())):
    n = int(input())
    l = 0
    for i in range(n):
        while True:
            l += 1
            x = decimalToTernary(l)
            if x.count('2') > len(x) / 2:
                print(x, end=' ')
                break
    print()