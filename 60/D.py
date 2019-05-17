# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,W = map(int,input().split())

w = [0 for i in range(N)]
v = [0 for i in range(N)]
for i in range(N):
    w[i],v[i] = map(int,input().split())

w_sum = [0 for i in range(N+1)]
v_sum = [0 for i in range(N+1)]

w.insert(0,0)
v.insert(0,0)

for i in range(N):
    w_sum[i+1] = w_sum[i]+w[i+1]
    v_sum[i+1] = v_sum[i]+v[i+1]


nap_memo = {}

def nap(i,W2):#i:count_pieces,W2:rest_weight
    key = str(i)+":"+str(W2)
    if key in nap_memo:
        return nap_memo[key]
    elif i == 0:#品物０個の時は価値０
        r = 0
    elif W2 < w[0]:
        r = 0
    elif W2 < w[i]:#i番目の荷物が残量を超えるなら入らない
        r = nap(i-1,W2)
    elif w_sum[i] <= W2:
        r = v_sum[i]
    else:
        r = max(nap(i-1,W2-w[i])+v[i], nap(i-1,W2))

    nap_memo[key] = r
    return r


print(nap(N,W))
#
# dp = [[[0 for i in range(W+1)] for j in range(N)]
#
#
# for i in range(N):
#     if N < w[i]:
#         pass
#     else:
#         dp[i][w[i]] = v[i]
#     for j in range(W+1):
#         if i-1 >= 0:
#             dp[i][j] = max(dp[i][j],dp[i-1][j])
#         if j-w[i] >= 0:
#             dp[i][j] = max(dp[i][j],dp[i-1][j-w[i]]+v[i])
#
# print(max(dp[-1]))
