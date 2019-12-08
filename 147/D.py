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

N = int(input())
A = LI()

count_list = [0 for i in range(61)]
def counts(count_list, a):
    for i in range(61):
        if a <= 0:
            break
        count_list[i] += a % 2
        a = a // 2
    return count_list

A.reverse()
ans = 0
ans_list = [0 for i in range(61)]
for i in range(N-1):
    count_list = counts(count_list, A[i])
    hikaku = counts([0 for i in range(61)], A[i + 1])
    for j in range(61):
        if hikaku[j] == 1:
            ans_list[j] += i+1 - count_list[j]
        else:
            ans_list[j] += count_list[j]

for i in range(61):
    ans += ans_list[i] * (2 ** i % mod)
    ans = ans % mod
print(ans)
