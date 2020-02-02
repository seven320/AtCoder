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

H,W = LI()
S = [[] for i in range(H)]
for i in range(H):
    S[i] = list(str(input()))

graph = [[] for i in range(H * W)]
moves = [[0,1], [1,0], [0,-1],[-1,0]]
for h in range(H):
    for w in range(W):
        if S[h][w] == ".":
            for move in moves:
                next_h = h + move[0]
                next_w = w + move[1]
                if -1 < next_h < H and -1 < next_w < W:
                    if S[next_h][next_w] == ".":
                        graph[h * W + w].append(next_h*W + next_w)

# print(graph)
N = H*W
dp = [[mod for i in range(N)] for j in range(N)]
for i in range(N):
    dp[i][i] = 0
for i in range(N):
    for edge in graph[i]:
        dp[i][edge] = 1
        dp[edge][i] = 1
for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
ans = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] != mod:
            ans = max(ans, dp[i][j])
print(ans)
