# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
import E


mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

def cnt_p(N):
    return cnt_paper(list(str(N)))

def cnt_paper(s):
    tmp = 0
        # print(s)
    for s_i in s:
        tmp += int(s_i)
    return tmp

for i in range(5,6):
    tmp_ans = mod
    for j in range(i,100):
        tmp_ans = min(tmp_ans, cnt_p(j) + cnt_p(j - i))
        print(tmp_ans)

    # print(tmp_ans)
    if tmp_ans != E.solve(i):
        print(tmp_ans, E.solve(i))
