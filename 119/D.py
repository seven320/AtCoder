# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect

mod = 10**13
# sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

A,B,Q = LI()
s = [0 for i in range(A)]
t = [0 for i in range(B)]
x = [0 for i in range(Q)]
for i in range(A):
    s[i] = int(input())
for i in range(B):
    t[i] = int(input())
for i in range(Q):
    x[i] = int(input())


def solve(pos):
    ans1,ans2,ans3,ans4 = mod,mod,mod,mod
    s_left = bisect.bisect_left(s,pos)-1
    t_left = bisect.bisect_left(t,pos)-1
    # print("s",s_left,"t",t_left)
    if s_left >= 0 and t_left >= 0:
        ans1 = pos - min(s[s_left],t[t_left])
    if s_left+1 < A and t_left >= 0:
        ans2 = s[s_left+1] - t[t_left] + min(s[s_left+1]-pos, pos - t[t_left])
    if t_left + 1 < B and s_left>= 0:
        ans3 = t[t_left+1] - s[s_left] + min(t[t_left+1] - pos, pos-s[s_left])
    if s_left+1 < A and t_left+1 < B:
        ans4 = max(s[s_left+1],t[t_left+1]) - pos
    # print(ans1,ans2,ans3,ans4)
    ans = min(ans1,ans2,ans3,ans4)
    return ans


for i in range(Q):
    print(solve(x[i]))
