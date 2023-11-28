import datetime
time = datetime.datetime.strptime('6:00', '%H:%M')
S = 120
unit = 'Km/h'

class Candidate:
    def __init__(self, name, office, complete) -> None:
        self.name = name
        self.office = office
        self.cplTime = datetime.datetime.strptime(complete, '%H:%M')
        self.id = self.getID()
        self.v = S / ((self.cplTime - time).seconds / 3600)

    def getID(self):
        return ''.join([x[0].upper() for x in (self.office+' '+self.name).split()])
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.office} {round(self.v)} {unit}'

n = int(input())
candidates = []
for _ in range(n):
    name = input()
    office = input()
    complete = input().strip()
    candidates.append(Candidate(name, office, complete))
candidates.sort(key= lambda x: x.v, reverse=True)
print(*candidates, sep='\n')
