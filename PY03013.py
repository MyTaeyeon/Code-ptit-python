'''
Cho 2 số nguyên A, B. 
Nhiệm vụ của bạn là hãy đếm xem mỗi chữ số sẽ xuất hiện
 bao nhiêu lần nếu như liệt kê tất cả các số từ A đến B.
'''

def dfs(number, a, base):
    if number <= 0:
        return

    ans = number % 10
    pos = number // 10

    for i in range(1, ans + 1):
        a[i] += base
    
    while pos > 0:
        a[pos % 10] += (ans + 1) * base
        pos //= 10
    
    for i in range(10):
        a[i] += (number // 10) * base
    
    dfs(number // 10 - 1, a, base * 10)

for _ in range(int(input())):
    [n, m] = list(map(int, input().split()))

    a = [0] * 10
    b = [0] * 10

    dfs(n - 1, a, 1)
    dfs(m, b, 1)

    print(*[b[i] - a[i] for i in range(10)])