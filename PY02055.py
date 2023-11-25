m, n = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(m)]
ans = list
max_prime_num = -1

def isPrime(x):
    if x < 2: return False
    else:
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0: return False
        return True

for i in range(m):
    for j in range(n):
        if isPrime(matrix[i][j]) == True:
            if matrix[i][j] > max_prime_num:
                max_prime_num = matrix[i][j]
                ans = [[i, j]]
            elif matrix[i][j] == max_prime_num:
                ans.append([i, j])

if max_prime_num == -1:
    print('NOT FOUND') 
else:
    print(max_prime_num)
    for x in ans:
        print(f'Vi tri [{x[0]}][{x[1]}]')
