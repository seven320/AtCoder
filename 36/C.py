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
a = [0 for i in range(N)]
for i in range(N):
    a[i] = int(input())

b = copy.deepcopy(a)
b.sort()
pre = -1
exchange_dic = {}
cnt = 0
for i in range(N):
    if pre != b[i]:
        exchange_dic[b[i]] = cnt
        cnt += 1
        pre = b[i]

# print(exchange_dic)
for i in range(N):
    print(exchange_dic[a[i]])
