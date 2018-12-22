S = input()
T = input()
s = list(S)
t = list(T)
match = False
for rotation in range(len(s)):
    flag = 0
    for i in range(len(s)):
        if i+rotation > len(s)-1:
            count = i+rotation-len(s)
        else:
            count = i+rotation
        if s[count] == t[i]:
            pass
        else:
            flag = 1
    if flag == 0:
        match = True
if match == True:
    print("Yes")
else:
    print("No")
