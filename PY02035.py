s = input()
k = int(input())
a = []
for i in range(len(s)//2):
    b = int(s[i*2]) * 10 + int(s[i*2+1])
    a.append(b)
tmp = [0] * 100
b = []
for i in range(len(a)):
    if ( tmp[a[i]] == 0 and a.count(a[i]) >= k ):
        tmp[a[i]] = 1
        b.append(a[i])
if ( len(b) == 0 ):
    print("NOT FOUND")
else:
    b.sort()
    for i in range(len(b)):
        print(b[i], a.count(b[i]))
