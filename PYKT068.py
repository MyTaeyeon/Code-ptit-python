class ExamSubject:
    def __init__(self, ID, name, form) -> None:
        self.id = ID
        self.name = name
        self.form = form

    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.form}'

n = int(input())
subjects = []
for i in range(n):
    id = input()
    name = input()
    form = input()
    subjects.append(ExamSubject(id, name, form))
subjects.sort(key=lambda x: x.id)
print(*subjects, sep='\n')
