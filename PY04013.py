import datetime
import math

class rainRecord:
    def __init__(self, id, name) -> None:
        self.id = 'T{:02d}'.format(id)
        self.stationName = name
        self.total_time = 1
        self.total_rainfall = 0

    def __str__(self) -> str:
        return f'{self.id} {self.stationName} {math.ceil((self.total_rainfall/(self.total_time/3600))*100)/100:.2f}'

    def timediff(self, start, end):
        start = datetime.datetime.strptime(start, '%H:%M')
        end = datetime.datetime.strptime(end, '%H:%M')

        time_difference = end - start

        return time_difference.seconds
    
    def update(self, start, end, rainfall):
        self.total_time += self.timediff(start, end)
        self.total_rainfall += rainfall
    
station = []
uniquename = dict()
l = 0
for _ in range(int(input())):
    name = input()
    start_time = input()
    end_time = input()
    rainfall = int(input())

    if name not in uniquename:
        uniquename[name] = len(station)
        station.append(rainRecord(uniquename[name] + 1, name))

    station[uniquename[name]].update(start_time, end_time, rainfall)

print(*station, sep='\n')