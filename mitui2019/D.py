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
S = list(str(input()))

ans = 0
for i in range(1000):
    nums = list(str(i).zfill(3))
    fir = 0
    cnt = 0
    for num in nums:
        try:
            fir = S[fir:].index(num) + fir + 1
            cnt += 1
        except:
            break
    if cnt == 3:
        # print(str(i).zfill(3))
        ans += 1

print(ans)
