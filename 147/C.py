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

N = int(input())
A = [0 for i in range(N)]
xy = [[] for i in range(N)]
value = [[] for i in range(N)]
for i in range(N):
    A[i] = int(input())
    for j in range(A[i]):
        x,y = LI()
        x -= 1
        xy[i].append([x,y])

def make2digits(n):
    digits = [0 for i in range(N)]
    i = 0
    while n > 0:
        digits[i] = n % 2
        n = n // 2
        i += 1
    return digits

def check(digits, xy):
    for i in range(N):
        if digits[i] == 1:
            for signal in xy[i]:
                if digits[signal[0]] == signal[1]:
                    pass
                else:
                    return False
    return True
ans = -1
for i in range(2**N):
    digits = make2digits(i)
    if check(digits, xy):
        ans = max(ans, sum(digits))

print(ans)
