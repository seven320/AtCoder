# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

S = str(input())
count = {}
for i in range(len(S)):
    if S[i] in count.keys():
        count[S[i]] += 1
    else:
        count[S[i]] = 1

flag = True
for key in count.keys():
    if count[key] == 2:
        pass
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")
