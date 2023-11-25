def transform_matrix(N, M, matrix):
    while N > M:
        loc_of_pop = range(0, min(N, 2*(N-M)), 2)
        N -= len(loc_of_pop)
        [matrix.pop(x) for x in loc_of_pop[::-1]]
    while M > N:
        loc_of_pop = range(1, min(M, 2*(M-N)+1), 2)
        M -= len(loc_of_pop)
        for row in matrix:
            [row.pop(x) for x in loc_of_pop[::-1]]
    [print(" ".join(map(str, row))) for row in matrix]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
transform_matrix(N, M, matrix)
