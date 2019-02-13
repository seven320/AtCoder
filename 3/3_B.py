
s = str(input())
t = str(input())

atcoder = list("atcoder")
for i in range(len(s)):
    if s[i] == "@" and t[i] in atcoder:
        pass
    elif t[i] == "@" and s[i] in atcoder:
        pass
    elif t[i] == s[i]:
        pass
    else:
        print("You will lose")
        exit()

print("You can win")
