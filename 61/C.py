# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,K = map(int,input().split())

# anss = [0 for i in range(K)]
inserts = [[] for i in range(N)]
for i in range(N):
    inserts[i] = [int(i) for i in input().split()]


inserts.sort()
cnt = 0
for insert in inserts:
    cnt += insert[1]
    ans = insert[0]
    # print(cnt)
    if cnt >= K:
        break

print(ans)
