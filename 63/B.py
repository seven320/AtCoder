# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7



S = str(input())
used = []
for i in range(len(S)):
    if S[i] in used:
        print("no")
        exit()
    else:
        used.append(S[i])
print("yes")