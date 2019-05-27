# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

M,K = map(int,input().split())
ans = False
if M == 0:
    if K == 0:
        ans = [0,0]
    else:
        print(-1)

elif M == 1:
    if K == 0:
        ans = [0,0,1,1]
    else:
        print(-1)

else:
    if K < 2**M:
        b = [int(i) for i in range(2**M)]
        b.remove(K)
        ans = []
        ans += b
        ans += [K]
        b.reverse()
        ans += b
        ans += [K]

    else:
        print(-1)
if ans == False:pass
else:
    for i in range(len(ans)):
        print(str(ans[i])+" ",end="")
    print("")
