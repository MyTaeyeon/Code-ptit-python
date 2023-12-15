movements = [[-1,-1], [-1,0], [-1,1], [0,1], [1, 1],[1,0], [1,-1],[0,-1]]

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
visited = [[False]*n for _ in range(m)]
ans = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == -1:
            for a in movements:
                if 0<=i+a[0]<m and 0<=j+a[1]<n and visited[i+a[0]][j+a[1]]==False:
                    visited[i+a[0]][j+a[1]] = True
                    ans += matrix[i+a[0]][j+a[1]]
print(ans)
