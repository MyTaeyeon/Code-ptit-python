import datetime

class Player:
    def __init__(self, id, name, start, end) -> None:
        self.id = id
        self.name = name
        self.total_time = self.timeDifference(start, end)

    def timeDifference(self, start, end):
        start_time = datetime.datetime.strptime(start, '%H:%M')
        end_time = datetime.datetime.strptime(end, '%H:%M')

        time_diff = end_time - start_time

        return time_diff
    
    def __str__(self) -> str:
        hours, remainder = divmod(self.total_time.seconds, 3600)
        return f'{self.id} {self.name} {hours} gio {remainder // 60} phut'
    
players = []
for _ in range(int(input())):
    id = input()
    name = input()
    start = input()
    end = input()
    players.append(Player(id, name, start, end))

players.sort(key=lambda x: x.total_time, reverse=True)

print(*players, sep='\n')