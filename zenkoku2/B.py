# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
import collections

mod = 998244353
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
D = LI()

if D[0] != 0:
    print(0)
    sys.exit()

if 0 in D[1:]:
    print(0)
    sys.exit()


D.sort()
c = collections.Counter(D)
ans = 1
parents = 1
before = -1
for key in c.keys():
    if before + 1 != key:
        print(0)
        sys.exit()
    ans *= parents**c[key]
    ans = ans % mod
    parents = c[key]
    before = key

print(ans)
