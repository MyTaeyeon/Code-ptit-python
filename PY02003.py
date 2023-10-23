import bisect
hamming = [0, 1]
two = three = five = 1
MAX = 1e18
newNum = 0
while newNum < MAX:
    newNum = min(2 * hamming[two], 3 * hamming[three], 5 * hamming[five])
    hamming.append(newNum)
    if newNum == 2 * hamming[two]:
        two += 1
    if newNum == 3 * hamming[three]:
        three += 1
    if newNum ==  5 * hamming[five]:
        five += 1

for _ in range(int(input())):
    n = int(input())
    x = bisect.bisect_left(hamming, n)
    if n != hamming[x]:
        print('Not in sequence')
    else:
        print(x)