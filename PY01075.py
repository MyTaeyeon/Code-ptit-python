import math
tests = int(input())
while tests > 0:
    tests -= 1
    costs = dict()
    distances = []
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    costs[a[0]] = c[0]
    distances.append(a[0])
    for i in range(1, n):
        if a[i] not in costs: 
            costs[a[i]] = c[i]
            distances.append(a[i])
        else: costs[a[i]] = min(costs[a[i]], c[i])

        for j in distances:
            d = math.gcd(j, a[i])
            cost = costs[j] + c[i]
            if d not in costs:
                costs[d] = cost
                distances.append(d)
            else: costs[d] = min(costs[d], cost)
    
    print(-1) if 1 not in costs else print(costs[1])
