n = input()
while len(n) > 1:
    n = str(int(n[0:len(n)//2]) + int(n[len(n)//2:]))
    print(n)
