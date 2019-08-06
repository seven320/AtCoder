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
S = list(str(input()))
N = len(S)

ans = [0 for i in range(N)]
# R
cnt = 0
for i in range(N):
    if S[i] == "R":
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i-1] += math.ceil(cnt / 2)
        cnt = 0

#L
# S.reverse()
for i in range(N-1,-1,-1):
    if S[i] == "L":
        cnt += 1
    else:
        ans[i] += cnt // 2
        ans[i+1] += math.ceil(cnt / 2)
        cnt = 0

for i in range(N):
    print(ans[i],end=" ")
print()
