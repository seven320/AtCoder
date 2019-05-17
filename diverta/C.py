# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N = int(input())
s = [0 for i in range(N)]
cnt = 0
chance = False
A_cnt = 0
B_cnt = 0
BA_cnt = 0
for i in range(N):
    s[i] = str(input())
    cnt += s[i].count("AB")
    if s[i][0] == "B" and s[i][-1]=="A":
        BA_cnt += 1
    elif s[i][0] == "B":
        B_cnt += 1
    elif s[i][-1] == "A":
        A_cnt += 1


if BA_cnt != 0 and A_cnt == 0 and B_cnt == 0:
    plus = BA_cnt - 1
elif BA_cnt != 0 and A_cnt == 0:
    plus = min(BA_cnt,BA_cnt+B_cnt)
elif BA_cnt != 0 and B_cnt == 0:
    plus = min(BA_cnt,BA_cnt+A_cnt)
else:
    plus = min(BA_cnt+A_cnt,BA_cnt+B_cnt)

cnt += plus

print(cnt)
