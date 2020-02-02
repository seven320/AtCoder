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

N, M = LI()
ans = [-1 for i in range(3)]
if N * 2 <= M <= N * 4:
    extra_legs = M - N * 2
    ans[2] = math.floor(extra_legs / 2)
    extra_legs -= ans[2] * 2
    ans[1] = extra_legs
    ans[0] = N - ans[1] - ans[2]
    print(ans[0], ans[1], ans[2])
else:
    print("-1 -1 -1")