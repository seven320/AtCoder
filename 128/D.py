# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,K = map(int,input().split())
V = [int(i) for i in input().split()]
#
# if N == 1:
#     print(max(0,V[0]))
#     exit()

ans = 0
for i in range(K): # 戻す数
    for j in range(K-i+1):
        if j <= N-(K-i-j):
            ans_list = V[:j]+V[N-(K-i-j):]
            ans_list.sort()
            tmp = sum(ans_list)
            for k in range(min(len(ans_list),i)):
                if ans_list[k] < 0:
                    tmp -= ans_list[k]
            ans = max(ans,tmp)
        else:
            pass

print(max(ans,0))
