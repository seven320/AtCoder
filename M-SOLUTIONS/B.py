# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000


S = str(input())
win = 0
for i in range(len(S)):
    if S[i] == "o":
        win += 1


if 15-len(S)+win >= 8:
    print("YES")
else:
    print("NO")
