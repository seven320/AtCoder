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

N,K = LI()
a = LI()

sum_now = 0
ans = 0
r = 0
# しゃくとり法
for l in range(N): # 左端固定
    while sum_now < K:
        if r == N:　# 右端が右についたら終わり
            break
        else:
            sum_now += a[r]
            r += 1
    if sum_now < K:
        break
    ans += N - r + 1 # 合計がsum_now以上になったものが対象なので右の部分をタス
    sum_now -= a[l] # しゃくとりなので左端が動くときには左を消去する
print(ans)
