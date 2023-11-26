n = int(input())
a = list(map(int, input().split()))
x = min(a)
ans = float('inf')

def roundUp(x):
    if int(x) == x:
        return x + 1
    else:
        return int(x+1)
for i in range(x, 0, -1):
    sum = 0
    for j in a:
        if roundUp(j/(i+1)) >= roundUp(j//i):
            sum = float('inf')
            break
        else:
            sum += roundUp(j/(i+1))
    ans = min(ans, sum)
print(int(ans))
