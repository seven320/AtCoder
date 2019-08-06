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

N = int(input())
a = LI()

left = mod
cnt = 0
ans = 0
for i in range(N):
    if left < a[i]:
        cnt += 1
    else:
        ans += cnt * (cnt + 1)//2
        cnt = 1
    left = a[i]
ans += cnt * (cnt + 1)//2

print(ans)
