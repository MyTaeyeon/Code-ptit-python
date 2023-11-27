class Pupil:
    def __init__(self, id, name, classID) -> None:
        self.id = id
        self.name = name
        self.classID = classID
        self.attendanceRating = 0

    def getAttendace(self):
        return str(self.attendanceRating) if self.attendanceRating > 0 else str(self.attendanceRating) + ' KDDK'

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.classID} {self.getAttendace()}'

n = int(input())
pupils = []
for _ in range(n):
    id = input()
    name = input()
    classID = input()
    pupils.append(Pupil(id, name, classID))

for _ in range(n):
    id, record = input().split()
    for j in pupils:
        if j.id == id:
            j.attendanceRating = max(0, 10 - 2 * record.count('v') - record.count('m'))
            break

print(*pupils, sep='\n')
