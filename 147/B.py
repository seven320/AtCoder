# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

S = str(input())

n = len(S)//2
cnt = 0
for i in range(n):
    if S[i] == S[-(i+1)]:
        pass
    else:
        cnt += 1
print(cnt)
