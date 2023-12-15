class Teacher:
    subject = {'A' : 'TOAN', 'B' : 'LY', 'C':'HOA'}
    plus = [0, 2.0, 1.5, 1.0, 0.0]
    def __init__(self, id, name, subID, *scores) -> None:
        self.id = f'GV{id:02d}'
        self.name = name
        self.major = self.subject[subID[0]]
        self.score = scores[0]*2 + scores[1] + self.plus[int(subID[1])]
        self.band = 'TRUNG TUYEN' if self.score > 18 else 'LOAI'
    
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.major} {self.score:.1f} {self.band}'
    
tests = int(input())
teachers = []
for i in range(1, tests+1):
    name = input()
    majorID = input()
    a = float(input())
    b = float(input())
    teachers.append(Teacher(i, name, majorID, a, b))

teachers.sort(key=lambda x: x.score, reverse=True)
print(*teachers, sep='\n')
