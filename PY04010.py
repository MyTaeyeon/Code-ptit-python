class Examinee:
    def __init__(self, name, date, scores) -> None:
        self.name = name
        self.date = date
        self.scores = scores
        self.total = sum(scores)

    def __str__(self) -> str:
        return f"{self.name} {self.date} {self.total:.1f}"
    
name = input()
date = input()
scores = [float(input()) for _ in range(3)]

a = Examinee(name, date, scores)
print(a)