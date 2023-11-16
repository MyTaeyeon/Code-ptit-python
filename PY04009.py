class complexNum:
    def __init__(self, a, b) -> None:
        self.real = a
        self.imaginary = b
    
    def __str__(self) -> str:
        if self.imaginary < 0:
            return f'{self.real} - {abs(self.imaginary)}i'
        else:
            return f'{self.real} + {abs(self.imaginary)}i'
    
def add(A, B):
    return complexNum(A.real + B.real, A.imaginary + B.imaginary)

def multiply(A, B):
    real = A.real * B.real - A.imaginary * B.imaginary
    imaginary = A.imaginary * B.real + A.real * B.imaginary
    return complexNum(real, imaginary)
    
for _ in range(int(input())):
    l = list(map(int, input().split()))
    A = complexNum(l[0], l[1])
    B = complexNum(l[2], l[3])

    C = multiply(add(A, B), A)
    D = multiply(add(A, B), add(A, B))

    print(C, D, sep=', ')
