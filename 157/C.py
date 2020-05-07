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

N, M = LI()
sc = []
for i in range(M):
    sc.append(LI())

ans = ["0" for i in range(N)]
ans_exist = True
if N == 1:
    for i in range(M):
        s,c = sc[i]
        s -= 1
        c = str(c)
        if ans[s] == "0":
            ans[s] = c
        elif ans[s] != "0" and ans[s] == c:
            pass
        else:
            ans_exist = False
            break

    if ans_exist:
        print("".join(ans))
    else:
        print("-1")

else:
    for i in range(M):
        s,c = sc[i]
        s -= 1
        c = str(c)
        if s == 0 and c == "0":
            ans_exist = False
            break

        if ans[s] == "0":
            ans[s] = c
        elif ans[s] != "0" and ans[s] == c:
            pass
        else:
            ans_exist = False
            break

    if ans_exist:
        if ans[0] == "0":
            ans[0] = "1"
        print("".join(ans))
    else:
        print("-1")