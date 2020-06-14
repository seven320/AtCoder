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

N, K = LI()
A = LI()

if K > 50:
    print(" ".join([str(N) for i in range(N)]))
    sys.exit()

for i in range(K):
    A_new = [0 for i in range(N)]
    imos_table = [0 for i in range(N)]

    for j in range(N):
        left = max(0, j - A[j])
        right = j + A[j] + 1
        imos_table[left] += 1
        if right >= N:
            pass
        else:
            imos_table[right] -= 1
    
    tmp = 0
    for j in range(N):
        tmp += imos_table[j]
        A_new[j] += tmp

    A = copy.deepcopy(A_new)

print(" ".join(map(str, A)))
    