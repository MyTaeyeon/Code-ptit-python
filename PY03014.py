for _ in range(int(input())):
    expression = input()
    stack = []
    curr = 0
    for x in expression:
        if x == '(':
            curr += 1
            stack.append(curr)
            print(stack[-1], end=' ')
        elif x == ')':
            print(stack[-1], end=' ')
            stack.pop()
    print()
