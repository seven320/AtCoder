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


N,A = LI()
x = LI()

# i,j,k i: i文字目まで
# j: それまで選んだ枚数
# k: 合計
# dp[i][j][k]: count


dp = [[[0 for k in range(sum(x))] for j in range(A+1)] for i in range(N+2)]

dp[0][0][0] = 1
for i in range(1,N+1):
    for j in range(1,A+1):
        for k in range(sum(x)):
            if j >= 1 and k < x[i-1]:
                dp[i][j][k] = dp[i-1][j][k]
            if j>= 1 and k>= 1 and k>=x[i-1]:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k-x[i-1]]


            # dp[i+1][j][k] += dp[i][j][k]
            # dp[i+1][j+1][k+x[i]] += dp[i][j][k]

print(dp)
ans = 0
for j in range(A+1):
    try:
        ans += dp[-1][j][A*(j)]
    except:
        pass
print(ans)
