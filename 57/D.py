# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math

mod = 10**9+7

N,A,B = map(int,input().split())
v = [int(i) for i in input().split()]


dp = [[0 for j in range(B+1)] for i in range(N)]
for i in range(N):
    dp[i][0] = max(v[:i+1])

for i in range(N-1):
    for j in range(min(B,i+1)):
        dp[i+1][j+1] = max(dp[i][j+1],(dp[i][j]*(j+1)+v[i+1])/(j+2))

ans = max(dp[-1][A-1:B+1])
# v.sort()
# v.reverse()
# ans = 0
# for i in range(A):
#     ans += v[i]
# ans /= A
print(ans)

v.sort()
v.reverse()

cnt = 0
if v[0] != v[A-1]:
    m = v.count(v[A-1])
    n = v[:A].count(v[A-1])
    cnt = math.factorial(m)//(math.factorial(n)*math.factorial(m-n))
else:
    m = v.count(v[0])
    n = A
    for i in range(n,B+1):
        if m-i < 0:
            pass
        else:
            cnt += math.factorial(m)//(math.factorial(i)*math.factorial(m-i))

print(cnt)
