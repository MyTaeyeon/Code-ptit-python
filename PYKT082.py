def bandScore(x):
    if 39<=x<=40:
        return 9.0
    elif 37<=x<=8:
        return 8.5
    elif 35<=x<=36:
        return 8.0
    elif 33<=x<=34:
        return 7.5
    elif 30<=x<=32:
        return 7.0
    elif 27<=x<=29:
        return 6.5
    elif 23<=x<=26:
        return 6.0
    elif 20<=x<=22:
        return 5.5
    elif 16<=x<=19:
        return 5.0
    elif 13<=x<=15:
        return 4.5
    elif 10<=x<=12:
        return 4.0
    elif 7<=x<=9:
        return 3.5
    elif 5<=x<=6:
        return 3.0
    elif 3<=x<=4:
        return 2.5
    else:
        return 0.0

for _ in range(int(input())):
    [reading, listening, speaking, writing] = list(map(float, input().split()))
    reading = bandScore(reading)
    listening = bandScore(listening)
    total = (reading + listening + speaking + writing) / 4
    remainer = total - int(total)
    if remainer < 0.25:
        total = int(total)
    elif remainer < 0.75:
        total = int(total) + 0.5
    else:
        total = int(total) + 1
    print('{:.1f}'.format(total))
