#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections
from decimal import Decimal # 10進数で考慮できる

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))
"""
N, K = LI()
A = LI()

def abssort(A):
    return sorted(A, key = lambda x:abs(x), reverse= True)

tmps = []
A_abs = abssort(A)
cnt = 0
while len(tmps) > K:
# for i in range(K):
    if A_abs[cnt] != 0:
        tmps.append(A_abs[i])
        cnt += 1

cnt = 0
for i in range(K):
    if tmps[i] < 0:
        cnt += 1
if cnt % 2 == 0:
    ans = 1
    for i in range(K):
        ans *= tmps[i]
        ans = ans % mod
    print(ans)
    sys.exit()
else:
    tmp_1 = copy.deepcopy(tmps)
    tmp_2 = copy.deepcopy(tmps)
    tmp_1.reverse()
    tmp_2.reverse()
    tmp_2_ = 0
    tmp_1_ = 0
    # -を一つ消す
    for i in range(K):
        if tmp_1[i] < 0:
            tmp_1.remove(tmp_1[i])
            break
    # + を一つたす
    for i in range(K, N):
        if A_abs[i] > 0:
            tmp_1.append(A_abs[i])
            tmp_1_ = 1
            break
    else:
        # +がなかった時
        tmp_1 = []
        tmp_1_ = -1 
        A_abs.reverse()
        for i in range(K):
            tmp_1.append(A_abs[i])

    # +を消して-を追加
    cnt = 0
    for i in range(K):
        if tmp_2[i] > 0:
            tmp_2.remove(tmp_2[i])
            cnt += 1
            break
    if cnt == 1:
        for i in range(K, N):
            if A_abs[i] < 0:
                tmp_2.append(A_abs[i])
                tmp_2_ = 1
                break
        else:
            tmp_2_ = 0
    else:
        tmp_2_ = -1
# print(tmp_1, tmp_2)



tmp_1_m = 1
tmp_2_m = 1
for i in range(K):
    tmp_1_m *= tmp_1[i]
    tmp_1_m = tmp_1_m % mod

if tmp_2_ == 0:
    pass
else:
    for i in range(K):
        tmp_2_m *= tmp_2[i]
        tmp_2_m = tmp_2_m % mod

# print(tmp_1_, tmp_2_)
if tmp_2_ == 0:
    print(tmp_1_m)
elif tmp_1_ == 1 and tmp_2_ == -1:
    print(tmp_1_m)
elif tmp_1_ == -1 and tmp_2_ == 1:
    print(tmp_2_m)
elif tmp_1_ == 1 and tmp_2_ == 1:
    for i in range(K):
        if tmp_1[i] == tmp_2[i]:
            pass
        elif abs(tmp_1[i]) > abs(tmp_2[i]):
            print(tmp_2_m)
            sys.exit()
        else:
            print(tmp_1_m)
            sys.exit()
else:
    print(tmp_1_m)
    # for i in range(K):
    #     if tmp_1[i] == tmp_2[i]:
    #         pass
    #     elif abs(tmp_1[i]) > abs(tmp_2[i]):
    #         print(tmp_2_m)
    #         sys.exit()
    #     else:
    #         print(tmp_1_m)
    #         sys.exit()
    """

N,K = list(map(int, input().split()))
A = list(map(int, input().split()))

# 正負に関係なくsort
A_abs = sorted(A, key = lambda x:abs(x))
A_p = [] # plusを入れる
A_n = [] # -を入れる
for i in range(N):
    if A[i] < 0:
        A_n.append(A[i])
    else:
        A_p.append(A[i])

A_n.sort()
A_p.sort(reverse = True)

ok = True
if len(A_p) > 0:
    # 正の数が存在している
    if N == K:
        # 選択肢がない時
        ok = (len(A_n) % 2 == 0)
        # 負の数が偶数個
    else:
        ok = True
else:
    ok = (K % 2 == 0)

ans = 1
if ok == False:
    # 解が正にならない場合は絶対値でソートしたものの中で小さいものからかけていく
    for i in range(K):
        ans *= A_abs[i]
        ans = ans % mod
else:
    if K % 2 == 1:
        # 奇数個選ぶ
        ans *= A_p[0]
        ans = ans % mod
        A_p = A_p[1:]
    position = 0
    pairs = []
    cnt_p = len(A_p)
    cnt_n = len(A_n)
    while cnt_p - position > 1:
        pairs.append(A_p[position] * A_p[position + 1])
        position += 2
    position = 0
    while cnt_n - position > 1:
        pairs.append(A_n[position] * A_n[position + 1])
        position += 2

    pairs.sort(reverse=True)
    for i in range(K // 2):
        ans *= pairs[i]
        ans = ans % mod

print(ans)

