s = input()
cnt = 0
while(1):
    cnt += 1
    s = str( sum[ ord(i) - 48 for i in s ] )
    if len(s) == 1: break 
print(cnt)
