for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    check = True
    for i in range(len(a)):
        if a[i] > b[i]:
            check = False
            break
    
    print('YES') if check == True else print('NO')