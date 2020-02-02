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

N, Q = LI()
lr = []
for i in range(Q):
    l, r = LI()
    l -= 1
    r -= 1
    lr.append([l,r])

# いもす法
# 操作に関する情報を一回まとめてしまってから累積和を使う
imosu = [0 for i in range(N+1)]
for i in range(Q):
    l,r = lr[i]
    imosu[l] += 1
    imosu[r+1] -= 1
for i in range(N):
    imosu[i] = imosu[i] % 2
# print(imosu)
ans = [0 for i in range(N)]

cnt = 0
for i in range(N):
    cnt += imosu[i]
    print(cnt % 2,end="")
print("")
