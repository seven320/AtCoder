# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

S = str(input())

ans = 1
if len(S) % 2 == 0:
    for i in range(len(S)):
        if i % 2 == 0:
            if "h" == S[i]:
                pass
            else:
                ans = 0
        else:
            if "i" == S[i]:
                pass
            else:
                ans = 0
else:
    ans = 0

if ans:
    print("Yes")
else:
    print("No")
