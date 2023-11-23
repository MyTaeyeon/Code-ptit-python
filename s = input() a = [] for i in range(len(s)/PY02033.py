s = input()
a = []
for i in range(len(s)//2):
    b = int(s[i*2]) * 10 + int(s[i*2+1])
    a.append(b)
tmp = [0] * 100
b = []
for i in range(len(a)):
    if ( tmp[a[i]] == 0 ):
        tmp[a[i]] = 1
        print(a[i], end=' ')
