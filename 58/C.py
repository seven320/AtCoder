# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

n = int(input())
S = ["" for i in range(n)]
for i in range(n):
    S[i] = str(input())

share_count = {}
for c in S[0]:
    if c in share_count.keys():
        share_count[c] += 1
    else:
        share_count[c] = 1

for i in range(1,n):
    word = S[i]
    count = {}
    for c in word:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1

    for key in share_count.keys():
        if key in count.keys():
            share_count[key] = min(share_count[key],count[key])
        else:
            share_count[key] = 0

keys =  list(share_count.keys())
# keys = list(keys)
keys.sort()

ans =""
for key in keys:
    for j in range(share_count[key]):
        ans += str(key)


print(ans)
