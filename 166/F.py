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

N, A, B, C = LI()
s = []
for i in range(N):
    s.append(str(input()))

def solve(A, B, C, N):
    anss = []
    ans = True
    for i in range(N):
        if s[i] == "AB":
            if A == 0 and B == 0:
                ans = False
                return ans, anss
            elif A > B:
                anss.append("B")
                A -= 1
                B += 1
            else:
                anss.append("A")
                A += 1
                B -= 1
        elif s[i] == "AC":
            if A == 0 and C == 0:
                ans = False
                return ans, anss
            elif A > C:
                anss.append("C")
                A -= 1
                C += 1
            else:
                anss.append("A")
                A += 1
                C -= 1
        elif s[i] == "BC":
            if B == 0 and C == 0:
                ans = False
                return ans, anss
            elif B > C:
                anss.append("C")
                B -= 1
                C += 1
            else:
                anss.append("B")
                B += 1
                C -= 1
    return ans, anss

ans, anss = solve(A, B, C, N)
# print(anss)
if ans:
    print("Yes")
    for i in range(N):
        print(anss[i])
else:
    print("No")
