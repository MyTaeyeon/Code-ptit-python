s1 = list(input())
s2 = input()
p = int(input()) - 1
print(''.join(s1[:p]) + s2 + ''.join(s1[p:]))