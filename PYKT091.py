ans = ['']
with open('VANBAN.in') as file:
    words = []
    for line in file:
        words += line.strip().split()
    for x in words:
        if x not in ans and x == x[::-1]:
            if len(x) > len(ans[0]):
                ans = [x]
            elif len(x) == len(ans[0]):
                ans.append(x)
    for x in ans:
        print(x, words.count(x))
