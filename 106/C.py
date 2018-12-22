#encoding utf-8

s = list(input())
k = int(input())

for i in range(k):
    if s[i] != "1":

        moji = s[i]
        break
    else:
        if i+1 == k:
            moji = "1"

print(moji)
