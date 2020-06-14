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
 

"""
3
1 1 2
のパターンが例外だった
"""

N = int(input())
A = LI()
A.sort()

table = [0 for i in range(10 ** 6 + 1)]
cnt = 0

# ダブっている値をまとめて保持
cc = collections.Counter(A)
duplicate = []
for key in cc.keys():
    if cc[key] > 1:
        duplicate.append(key)

# アリストテレスのふるいをboolで実装
for a in A:
    if table[a] != 0:
        pass
    else:
        if a not in duplicate:
            cnt += 1
        for i in range(1, 10 ** 6 + 1):
            if a * i > 10 ** 6:
                break
            table[a * i] = 1
            
print(cnt)
