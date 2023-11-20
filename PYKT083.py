tax = {'Xe_con 5':10000,
        'Xe_con 7':15000,
        'Xe_tai 2':20000,
        'Xe_khach 29':50000,
        'Xe_khach 45':70000}

ans = dict()
for _ in range(int(input())):
    lines = input().split()
    if lines[3] == 'OUT':
        continue
    else:
        ans[lines[4]] = ans.setdefault(lines[4], 0) + tax[lines[1] + ' ' + lines[2]]

for key, value in ans.items():
    print(key + ':', value)