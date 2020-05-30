# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
S = str(input())

cnt = 0
cnt += S.count("R") * S.count("G") * S.count("B")

# for i in range(1, N - 1):
#     for j in range(i + 1, N):
#         k = 2 * j - i
#         if k > N :
#             continue
#         if S[i - 1] != S[j - 1] and S[j-1] != S[k-1] and S[i -1] != S[k-1]:
#             cnt -= 1

for k in range(N):
    for j in range(k):
        i = 2 * j - k
        if i < 0:
            continue
        if S[i] != S[j] and S[j] != S[k] and S[i] != S[k]:
            cnt -= 1 

print(cnt)
