#encoding utf-8

n = int(input())
s = list(str(input()))

maxcha = 0
for i in range(n):
    left = set(s[:i])
    right = set(s[i:])
    now = len(left & right)
    maxcha = max(maxcha,now)
    # print(now)

print(maxcha)
