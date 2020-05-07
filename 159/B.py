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

S = str(input())

N = len(S)
ans = 1

def check(strs):
    n = len(strs)
    for i in range(n // 2 + 1):
        if strs[i] == strs[-1-i]:
            pass
        else:
            return False
    
    return True

# print(S[:(N - 1) // 2])
# print(S[(N + 3) //2-1 :])

S_b = S[:(N -1) //2]
S_a = S[(N + 3) // 2 - 1:]

if check(S) and check(S_b) and check(S_a):
    print("Yes")
else:
    print("No")
