# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

ans = -1
A_ = Counter(A)
cnt = 0
if N % 2 == 1:
    if A_[0] != 1:
        ans = 0
    for i in range(2,N,2):
        if A_[i] != 2:
            ans = 0
            break
        cnt += 1
else:
    for i in range(1,N,2):
        if A_[i] != 2:
            ans = 0
            break
        cnt += 1

if ans == 0:
    print(ans)
else:
    print(2**cnt%mod)
