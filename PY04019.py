idx = 1
class staff:
    scoreFormat = lambda x: x if x <= 10 else x / 10

    def __init__(self, name, *scores) -> None:
        global idx
        self.id = f'TS0{idx:d}'
        idx += 1
        self.name = name
        self.score = (staff.scoreFormat(scores[0]) + staff.scoreFormat(scores[1])) / 2
        self.band = self.type(self.score)

    def type(self, score):
        if score < 5:
            return 'TRUOT'
        elif score < 8:
            return 'CAN NHAC'
        elif score < 9.5:
            return 'DAT'
        else:
            return 'XUAT SAC'
        
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.score:.2f} {self.band}'

candidates = []
tests = int(input())
for i in range(tests):
    name = input()
    sc1 = float(input())
    sc2 = float(input())
    candidates.append(staff(name, sc1, sc2))

candidates.sort(key=lambda x: x.score, reverse=True)

print(*candidates, sep='\n')
