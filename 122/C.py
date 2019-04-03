# encoding:utf-8
import copy
import numpy as np
import random
#

# n,q = map(int,input().split())
# s = list(str(input()))
# L = []
# for i in range(q):
#     l,r = map(int,input().split())
#     L.append([l,r])
#
# # count_ac = np.zeros([n])
# count_ac = []
# count = 0
# i = 0
# while i < n-1:
#     if s[i] == "A" and s[i+1] == "C":
#         count_ac.append(count)
#         count += 1
#         count_ac.append(count)
#         i += 2
#     else:
#         count_ac.append(count)
#         i += 1
#
# count_ac.append(count)
#
#
# # print(count_ac)
# for i in range(q):
#     ans = count_ac[L[i][1]-1]-count_ac[L[i][0]-1]
#     print(int(ans))

N,Q = map(int,input().split())
S = input()
t = [0 for i in range(N+1)]
for i in range(N):
    t[i+1] = t[i] + (1 if S[i:i+2]=="AC" else 0)
for i in range(Q):
    l,r = map(int,input().split())
    print(t[r-1]-t[l-1])
