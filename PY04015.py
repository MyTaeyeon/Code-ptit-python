import decimal

class bill:
    def __init__(self, id, name, numbers) -> None:
        self.customer_name = name
        self.id = f'KH{id:02d}'
        self.charge = decimal.Decimal(self.calc(numbers)).quantize(decimal.Decimal('0'), decimal.ROUND_HALF_UP)

    def calc(self, x):
        if x <= 50:
            return x * 100 * 1.02
        elif x <= 100:
            return (5000 + (x - 50) * 150) * 1.03
        else:
            return (5000 + 7500 + (x - 100) * 200) * 1.05
        
    def __str__(self) -> str:
        return f'{self.id} {self.customer_name} {self.charge}'

customers = []
for i in range(1, int(input()) + 1):
    name = input().strip()
    before = int(input())
    after = int(input())
    customers.append(bill(i, name, after - before))

customers.sort(key=lambda x: x.charge, reverse=True)

print(*customers, sep='\n')