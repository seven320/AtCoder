# encoding:utf-8
import copy
import numpy as np
import random

N = int(input())
MOD = 10**9+7
memo = [{} for i in range(N+1)]

def check(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i-1],t[i] = t[i],t[i-1]

        if "".join(t).count("AGC") >= 1:
            return False

    return True

def dfs(cur,last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0
    for c in "AGCT":
        if check(last3+c):
            ret = (ret + dfs(cur+1,last3[1:]+c))%MOD
    memo[cur][last3] = ret
    return ret

print(dfs(0,"TTT"))
# for i in range(N):
#     print(memo[i])
# print(memo)
