words = []
with open('DATA.in') as file:
    for line in file:
        a = line.strip().split()
        for x in a:
            if x.isdigit() == True:
                if int(x) < 2**32:
                    pass
                else:
                    words.append(x)
            else:
                words.append(x)
words.sort()
print(*words)
