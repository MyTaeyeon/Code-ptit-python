def minMove(begin, curr, length):
    curr -= begin
    if curr < 0: 
        curr += length
    return curr

n = int(input())    
words = [input().strip() for _ in range(n)]
id = [0] * n

no = False
for i in range(1, n):
    while words[i] != words[0] and id[i] < len(words[0]):
        words[i] = words[i][1:] + words[i][0]
        id[i] += 1
    if id[i] == len(words[0]):
        no = True

if no == False:
    ans = float('inf')
    for i in range(0, len(words[0])):
        k = 0
        for j in id:
            k += minMove(i, j, len(words[0]))
        ans = min(ans, k)
    print(ans)
else:
    print(-1)