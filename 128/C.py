# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,M = map(int,input().split())
k = [0 for i in range(M)]
s = [[] for i in range(M)]
for i in range(M):
    input_list = [int(i) for i in input().split()]
    k[i] = input_list[0]
    s[i] = input_list[1:]

p = [int(i) for i in input().split()]

def tobinary(i):
    l = [0 for j in range(N)]
    for k in range(N):
        l[k] = i % 2
        i //= 2
    return l

ans = 0
for i in range(2**N):
    swich = tobinary(i)
    for m in range(M):
        cnt = 0
        for k_i in range(k[m]):
            if swich[s[m][k_i]-1]:
                cnt += 1
        if cnt % 2 == p[m]:
            blight = True
        else:
            blight = False
            break
    if blight == True:
        ans += 1

print(ans)
