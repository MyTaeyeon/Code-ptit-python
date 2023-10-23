for _ in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    times = dict({})
    for i in numbers:
        times.setdefault(i, 0)
        times[i] += 1
    max_val = max(times.values())
    if max_val <= n / 2:
        print('NO')
    else:
        all_keys = [key for key, value in times.items() if value == max_val]
        print(min(all_keys))