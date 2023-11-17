characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(number, base):
    ans = ''
    while number > 0:
        ans += characters[number % base]
        number //= base
    return ans[::-1]

for _ in range(int(input())):
    [number, base] = list(map(int, input().split()))

    print(convert(number, base))