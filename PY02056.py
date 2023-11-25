m, n = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(m)]
ans = list
max_palindrom_num = -1

for i in range(m):
    for j in range(n):
        if matrix[i][j] > 9 and str(matrix[i][j]) == str(matrix[i][j])[::-1]:
            if matrix[i][j] > max_palindrom_num:
                max_palindrom_num = matrix[i][j]
                ans = [[i, j]]
            elif matrix[i][j] == max_palindrom_num:
                ans.append([i, j])

if max_palindrom_num == -1:
    print('NOT FOUND') 
else:
    print(max_palindrom_num)
    for x in ans:
        print(f'Vi tri [{x[0]}][{x[1]}]')
