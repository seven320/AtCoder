# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,A,B = map(int,input().split())
X = [int(i) for i in input().split()]

X.sort()
ans = (X[-1]-X[0])*A
for i in range(N-1):
    if (X[i+1] - X[i])*A > B:
        ans += B - (X[i+1] - X[i])*A
print(ans)
