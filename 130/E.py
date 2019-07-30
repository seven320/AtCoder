# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

N,M = LI()
S = LI()
T = LI()

dp = [[0 for i in range(M+2)] for j in range(N+2)]

for i in range(N+1):
    dp[i][0] = 1
for j in range(M+1):
    dp[0][j] = 1

for i in range(1,N+1):
    for j in range(1,M+1):
        tmp = 0
        if S[i-1] == T[j-1]:
            tmp = 1
        dp[i][j] = dp[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + tmp
print(dp)
print(dp[N-1][M-1])
