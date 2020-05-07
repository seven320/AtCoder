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

S = str(input())
Q = int(input())
q = [0 for i in range(Q)]
for i in range(Q):
    q[i] = list(input().split(" "))
# print(q)

status = True # True: normal, False: reversed
ans = collections.deque()
for s in list(S):
    ans.append(s)
for i in range(Q):
    query = q[i]
    if query[0] == "1":
        status = not(status)
    else:
        if query[1] == "1":
            if status:
                ans.appendleft(query[2])
            else:
                ans.append(query[2])
        else:
            if status:
                ans.append(query[2])
            else:
                ans.appendleft(query[2])
if status:
    print("".join(list(ans)))
else:
    print("".join(reversed(list(ans))))
