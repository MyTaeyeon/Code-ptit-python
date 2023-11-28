import datetime

class Customer:
    def __init__(self, id, name, roomID, rentDate, rvcDate, exp) -> None:
        self.id = f'KH{id:02d}'
        self.name = name
        self.roomID = roomID
        self.rentDate = datetime.datetime.strptime(rentDate, '%d/%m/%Y')
        self.rvcDate = datetime.datetime.strptime(rvcDate, '%d/%m/%Y')
        self.dayRent = self.diffTime()
        self.exp = exp
        self.totalCharge = self.dayRent*self.getFloorID() + self.exp

    def diffTime(self):
        time_difference = self.rvcDate - self.rentDate
        return time_difference.days + 1

    def getFloorID(self):
        if self.roomID[0] == '1':
            return 25
        elif self.roomID[0] == '2':
            return 34
        elif self.roomID[0] == '3':
            return 50
        else:
            return 80

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.roomID} {self.dayRent} {self.totalCharge}'

n = int(input())
customers = []
for i in range(1, n+1):
    name = input().strip()
    roomid = input().strip()
    rentdate = input().strip()
    rvcdate = input().strip()
    exp = int(input())
    customers.append(Customer(i, name, roomid, rentdate, rvcdate, exp))

customers.sort(key = lambda x: x.totalCharge, reverse=True)
print(*customers, sep='\n')
