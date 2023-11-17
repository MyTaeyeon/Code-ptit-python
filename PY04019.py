class staff:
    scoreFormat = lambda x: x if x <= 10 else x / 10

    def __init__(self, id, name, sc1, sc2) -> None:
        self.id = f'TS{id:02d}'
        self.name = name
        self.score = (staff.scoreFormat(sc1) + staff.scoreFormat(sc2)) / 2

    def type(self, score):
        if score < 5:
            return 'TRUOT'
        elif score < 8:
            return 'CAN NHAC'
        elif score < 9.5:
            return 'DAT'
        else:
            return 'XUAT XAC'
        
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.score:.2f} {self.type(self.score)}'

candidates = []
for i in range(1, int(input()) + 1):
    name = input()
    sc1 = float(input())
    sc2 = float(input())
    candidates.append(staff(i, name, sc1, sc2))

candidates = sorted(candidates, key=lambda x: x.score, reverse=True)

print(*candidates, sep='\n')