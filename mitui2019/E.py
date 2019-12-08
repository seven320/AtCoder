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

N = int(input())
A = LI()

ans = 1
cnts = [0,0,0]
for i in range(N):
    ans = ans * cnts.count(A[i]) % mod
    for j in range(3):
        if cnts[j] == A[i]:
            cnts[j] += 1
            break
print(ans)
