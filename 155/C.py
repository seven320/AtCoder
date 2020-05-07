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

N = int(input())
S = []
for i in range(N):
    S.append(str(input()))

c = collections.Counter(S)

max_c = -1
anss = []
for key, count in c.most_common():
    if max_c <= count:
        max_c = count
    else:
        break
    anss.append(key)
anss.sort()
for ans in anss:
    print(ans)