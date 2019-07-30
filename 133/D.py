# encoding:utf-8
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

mountains = [-1 for i in range(N)]
last = sum(A)//2
for i in range(0,N-1,2):
    last -= A[i]

mountains[-1] = last

for i in reversed(range(N-1)):
    mountains[i] = A[i] - mountains[i+1]

for i in range(N):
    print(mountains[i]*2,end=" ")
print("")
