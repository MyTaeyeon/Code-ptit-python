class Bill:
    def __init__(self, catogoryID, catogoryName, numbers, price, discount) -> None:
        self.catogoryID = catogoryID
        self.catogoryName = catogoryName
        self.numbers = numbers
        self.price = price
        self.discount = discount
        self.charge = price * numbers - discount
    
    def __str__(self) -> str:
        return f'{self.catogoryID} {self.catogoryName} {self.numbers} {self.price} {self.discount} {self.charge}'

tests = int(input())
bills = []
while tests > 0:
    tests -= 1
    id = input()
    name = input()
    numbers = int(input())
    price = int(input())
    discount = int(input())
    bills.append(Bill(id, name, numbers, price, discount))

bills.sort(key=lambda x: x.charge, reverse=True)
print(*bills, sep='\n')
