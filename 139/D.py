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

ans = 0
ans = (N - 1) * (N)//2

print(ans)


'''
1 0
2 1
3 3
4 6
5 10
6 15
7 21
8 28
9 36
10 45
11 55
12 66
13 78
'''
