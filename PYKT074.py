for _ in range(int(input())):
    line = input() + ' '
    notification = line[:min(len(line), 101)]
    while (notification[-1] != ' '):
        notification = notification[:-1]
    print(notification)