import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N,K = LI()
h = LI()
cnt = 0
for i in range(N):
    if h[i] >= K:
        cnt += 1
print(cnt)