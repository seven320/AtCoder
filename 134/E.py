# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
from collections import deque

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
N = int(input())
A = [0 for i in range(N)]
for i in range(N):
    A[i] = int(input())

ans = 1
tops = deque([A[0]])
tops_cnt = 1
for i in range(1,N):
    # print(tops)
    swap_i = bisect.bisect_left(tops,A[i])
    if swap_i:
        tops[swap_i-1] = A[i]
    else:
        tops.appendleft(A[i])
        ans += 1
        tops_cnt += 1

print(ans)
