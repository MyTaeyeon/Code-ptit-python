
class AddressBook:
    def __init__(self, name, numbers, date) -> None:
        self.name = name
        self.numbers = numbers
        self.date = date

    def __str__(self) -> str:
        return f'{self.name}: {self.numbers} {self.date}'

myAddBook = []
with open('SOTAY.txt', 'r') as file:
    day = ''
    name = ''
    numbers = ''
    for k in file:
        line = k.strip()
        if line[:4] == 'Ngay':
            day = line[5:]
        elif name == '':
            name = line
        else:
            numbers = line
            myAddBook.append(AddressBook(name, numbers, day))
            name = ''
            numbers = ''

myAddBook.sort(key=lambda x: (x.name.split()[-1], x.name))
with open('DIENTHOAI.txt', 'w') as file:
    [file.write(str(i) + '\n') for i in myAddBook]