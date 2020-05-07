# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import itertools
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))
N, M, Q = LI()

abcd = []

all = 0
for i in range(Q):
    a, b, c, d = LI()
    a -= 1
    b -= 1
    abcd.append([a, b, c, d])
    all += d

abcd = sorted(abcd, key= lambda x:x[3], reverse= True)
ans = 0
if Q <= 2:
    for q in range(Q):
        ans += abcd[q][-1]
    print(ans)
    sys.exit()

def cal_ans(A):
    ans = 0
    for i in range(Q):
        a, b, c, d = abcd[i]
        if A[b] - A[a] == c:
            ans += d
    return ans

def n2kdigit(n, k):
    bi=''
    before = 1
    while n!=0:
        if before <= (n % k):
            # print(n)
            bi+=str(n%abs(k))
            before = n % k
            if k<0:n=-(-n//k)
            else:n=n//k
        else:
            return None
    if len(bi) < N:
        return None
    return bi
ans = 0

for i in itertools.combinations_with_replacement(range(1, M+1), N):
    # print(i)
    ans = max(ans, cal_ans(i))
print(ans)