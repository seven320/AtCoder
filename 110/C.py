#encoding utf-8
s = list(str(input()))
t = list(str(input()))

def str2num(words):
    used = []
    nums = []
    for i in range(len(words)):
        if words[i] in used:
            nums.append(used.index(words[i]))
        else:
            used.append(words[i])
            nums.append(used.index(words[i]))
    return nums


if str2num(s) == str2num(t):
    print("Yes")
else:
    print("No")
