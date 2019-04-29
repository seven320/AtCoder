# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import fractions
from functools import reduce
N = int(input())
A = [int(i) for i in input().split()]



L = [0 for i in range(N)]
R = [0 for i in range(N)]
L[0] = A[0]
R[-1] = A[-1]
for i in range(N-1):
    L[i+1] = fractions.gcd(L[i],A[i+1])

for j in reversed(range(N-1)):
    R[j] = fractions.gcd(A[j],R[j+1])

L.append(0)
L.insert(0,0)
R.append(0)
R.insert(0,0)

ans = 1
for i in range(N):
    # print(L[i],R[i+2])
    ans = max(ans,fractions.gcd(L[i],R[i+2]))

print(ans)







"""
嘘解法
def gcd(nums):
    return reduce(fractions.gcd,nums)

ans = 1
A.sort()
gcd1 = gcd(A)
for i in range(N):
    A[i] //= gcd1

ans *= gcd1

gcd2 = A[0]
for i in range(1,N):
    gcd2 = fractions.gcd(gcd2,A[i])
    if gcd2 == 1:
        key = i
        break

a = copy.deepcopy(A)
a.remove(A[0])
b = copy.deepcopy(A)
b.remove(A[key])

ans *= max(gcd(a),gcd(b))
print(ans)
"""
