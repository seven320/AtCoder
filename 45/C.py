# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

S = str(input())

ans = 0
N = len(S)
for i in range(1,N+1): # 文字数
    for j in range(N-i+1):
        left = max(len(S[:j])-1,0)
        right = max(len(S[j+i:])-1,0)

        ans += int(S[j:j+i]) * (2**(left+right))

print(ans)
