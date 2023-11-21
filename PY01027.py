n = input()
exc = ['0', '1', '2', '3', '4', '5', '7', '888', '9']
beauty = True
for x in exc:
    if x in n:
        beauty = False
print('YES') if beauty == True else print('NO')