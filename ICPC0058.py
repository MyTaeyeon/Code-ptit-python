def read():
    global N, M, u, v, road
    N, M, u, v = map(int, input().split())
    road = [[] for _ in range(N + 1)]
    for _ in range(M):
        A, B = map(int, input().split())
        road[A].append(B)

def init():
    global check, mark
    check = [0] * (N + 1)
    mark = [1] * (N + 1)

def find_similar():
    for i in range(1, N + 1):
        if check[i] == 1 and mark[i] == 1:
            mark[i] = 1
        else:
            mark[i] = 0

def DQ_QL(r, End):
    if r == End:
        find_similar()
    else:
        for v in road[r]:
            if check[v] == 0:
                check[v] = 1
                DQ_QL(v, End)
                check[v] = 0

def main():
    global N, M, u, v, road, check, mark
    t = int(input())
    while t > 0:
        t -= 1
        read()
        init()
        check[u] = 1
        DQ_QL(u, v)
        check[u] = 0
        count = sum(1 for i in range(1, N + 1) if i != u and i != v and mark[i] == 1)
        print(count)
        road = [[] for _ in range(101)]  # 100 không đủ, sử dụng 101 để đảm bảo đủ số đỉnh

if __name__ == "__main__":
    main()
