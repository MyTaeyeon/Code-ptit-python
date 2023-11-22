def limit(a):
    if a == '??':
        return range(10, 99)
    elif a[0] == '?':
        return [i * 10 + int(a[1]) for i in range(1, 10)]
    elif a[1] == '?':
        return [int(a[0]) * 10 + i for i in range(0, 10)]
    else:
        return [int(a)]
    
def solve(a, b, c, operator):
    for x in a:
        for y in b:
            for z in c:
                for o in operator:
                    if o == '+':
                        if x + y == z:
                            return f'{x} + {y} = {z}'
                    elif o == '-':
                        if x - y == z:
                            return f'{x} - {y} = {z}'
                    elif o == '*':
                        if x * y == z:
                            return f'{x} * {y} = {z}'
                    else:
                        if x / y == z:
                            return f'{x} / {y} = {z}'
    return 'WRONG PROBLEM!'

for _ in range(int(input())):
    [a, operator, b, _, c] = input().split()
    a = limit(a)
    b = limit(b)
    c = limit(c)
    operator = list('+-*/') if operator == '?' else [operator]

    print(solve(a, b, c, operator))
