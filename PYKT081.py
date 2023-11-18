def check(a):
    arr = a.split(".")
    if len(arr) != 4 : return False
    for i in arr:
        try:
            if 0 > int(i) or int(i) > 255:
                return False
        except ValueError:
            return False
    return True

for _ in range(int(input())):
    string = input()
    print("YES") if check(string) == True else print("NO") 