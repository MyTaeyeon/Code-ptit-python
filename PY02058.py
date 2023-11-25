m, n = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(m)]
ans = list()
max_value = max([max(row) for row in matrix])
min_value = min([min(row) for row in matrix])
lucky_num = max_value - min_value
for i in range(m):
    for j in range(n):
        if matrix[i][j] == lucky_num:
            ans.append([i, j])

if len(ans) == 0:
    print('NOT FOUND') 
else:
    print(lucky_num)
    for x in ans:
        print(f'Vi tri [{x[0]}][{x[1]}]')
