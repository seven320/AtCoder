# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

s = str(input())
for i in range(len(s)):
    if s[i] == "A":
        start = i
        break

for i in reversed(range(len(s))):
    if s[i] == "Z":
        end = i
        break
print(end-start+1)
