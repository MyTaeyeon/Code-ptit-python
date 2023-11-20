subjects = []
numbers = []
tar = 0
for _ in range(int(input())):
    if tar == 0:
        subjects.append(input())
        numbers.append(0)
        tar = 1
    else:
        line = input().split()
        if len(line) != 0:
            numbers[-1] += 1
        else:
            tar = 0

for i in range(len(subjects)):
    print(subjects[i] + ': ' + str(numbers[i]))