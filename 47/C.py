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

ans_w = 0
cnt = [0,0] # W,B
left = S[0]
if left == "B":
    cnt[1] += 1
else:
    cnt[0] += 1
for i in range(1,len(S)):
    if left == S[i]:
        pass
    else:
        left = S[i]
        if left == "B":
            cnt[1] += 1
        else:
            cnt[0] += 1

if cnt[0] == cnt[1]:
    ans = (cnt[0] - 1) * 2 + 1

else:
    ans = min(cnt)*2
print(ans)
