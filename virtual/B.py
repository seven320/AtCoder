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

A,B,X = LI()

around_ans = min(min((X // A) + 1, 10**9) , X//B + 1)
# around_ans = min((X//A) + 1, 10**9)

def check_value(n):
    return X >= A*n + len(str(n)) * B

ans = 0
for i in range(around_ans):
     if check_value(around_ans - i):
         ans = max(around_ans - i, ans)
         break

print(ans)
