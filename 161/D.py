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

K = int(input())

lunluns = collections.deque()
for i in range(1, 10):
    lunluns.append(str(i))

for i in range(K - 9):
    a = lunluns[i]
    if a[-1] == "9":
        for j in ["8", "9"]:
            lunluns.append(a + j)
    elif a[-1] == "0":
        for j in ["0", "1"]:
            lunluns.append(a + j)
    else:
        base = int(a[-1])
        for j in range(base - 1, base + 2):
            lunluns.append(a + str(j))

print(lunluns[K - 1])