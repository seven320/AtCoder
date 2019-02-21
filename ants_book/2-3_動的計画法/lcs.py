# encoding:utf-8
import copy
import numpy as np
import random

n,m = map(int,input().split())
s = list(str(input()))
t = list(str(input()))


dp = [[0 for i in range(n+1)] for j in range(m+1)]
for i in range(0,n):
    for j in range(0,m):
        if s[i]==t[j]:
            dp[i+1][j+1]=max(dp[i][j]+1,dp[i][j+1],dp[i+1][j])
        else:
            dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])


print(dp[-1][-1])

# # ALDS1_10_c
# # https://onlinejudge.u-aizu.ac.jp/problems/ALDS1_10_C
# def solve():
#     s = list(str(input()))
#     t = list(str(input()))
#     dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
#     for i in range(0,len(s)):
#         for j in range(0,len(t)):
#             if s[i]==t[j]:
#                 dp[i+1][j+1]=dp[i][j]
#             else:
#                 dp[i+1][j+1]=max(dp[i+1][j],dp[i][j+1])
#
#     return dp[-1][-1]
#
# n = int(input())
# ans = []
# for i in range(n):
#     ans.append(solve())
# for i in range(n):
#     print(ans[i])
