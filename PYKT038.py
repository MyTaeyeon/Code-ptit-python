num = input()
while len(num) % 3 != 0: num = '0' + num
print(*[int(num[i:i+3], 2)for i in range(0, len(num), 3)], sep='')