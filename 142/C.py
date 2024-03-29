import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
A = LI()

aA = [[] for i in range(N)]
for i in range(N):
    aA[i] = [i+1, A[i]]

aA = sorted(aA, key = lambda x:x[1])
for i in range(N):
    print(aA[i][0],end="")
    print(" ",end="")
print("")
