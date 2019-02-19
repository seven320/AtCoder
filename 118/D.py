# encoding:utf-8
import copy
import numpy as np
import random
#
# n,m = map(int,input().split())
# a = [int(i) for i in input().split()]
#
# translate_match=[2,5,5,4,5,6,3,7,6]
# match = []
# for i in range(m):
#     match.append(translate_match[a[i]-1])
#
# # def dp(amari,memory):
# #     for i in range(len(match)):
# #         if amari==match[i]:
# #             print(memory)
# #             break
# #         elif amari>match[i]:
# #             next = amari-match[i]
# #             memory[i] += 1
# #             dp(next,memory)
#
# # ちょうど i 本のマッチ棒を使って、条件を満たす整数を作るときの最大桁数
#
# dp = [0]+[-1]*n
#
#
# for left_match in range(1,n+1):
#     # print(dp)
#     for j in range(len(match)):
#         if match[j]<=left_match:
#             dp[i] = max(dp[i],dp[left_match-match[j]]*10+a[j])
#             print(dp)
#
#
# print(dp[1])

# def solve():
#     N, M = map(int, input().split())
#     A = [int(a) for a in input().split()]
#     L = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#     A.sort(reverse = True)
#     #print(A)
#     dp = [0] + ([-1]*N)
#     #print(dp)
#     for i in range(1, N+1):
#         for a in A:
#             if L[a] <= i:
#                 dp[i] = max(dp[i], dp[i-L[a]] * 10 + a)
#     #print(dp)
#     print(dp[-1])


if __name__=="__main__":
    solve()
