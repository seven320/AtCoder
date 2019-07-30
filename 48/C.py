# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

N,x = map(int,input().split())
a = [int(i) for i in input().split()]
part_sum = [0 for i in range(N)]

ans = 0
if a[0] > x:
    ans += a[0]-x
    a[0] = x
left = a[0]
for i in range(1,N):
    if left + a[i] > x:
        ans += left + a[i] - x
        a[i] = x - left
    left = a[i]


print(ans)

"""
1 6 1 2 0 4
1 0 1 0 0 1
0 1 0 1 0 1


"""
