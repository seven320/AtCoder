# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,M = map(int,input().split())

facterint = [1]
for i in range(1,max(N,M)+1):
    facterint.append(facterint[-1]*i%mod)


if abs(N-M) > 1:
    print(0)
    exit()

if N==M:
    ans = 2*facterint[N]*facterint[M]%mod
else:
    ans = facterint[N]*facterint[M]%mod

print(ans)
