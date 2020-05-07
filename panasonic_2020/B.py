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

H, W = LI()

ans = 0

if H == 1 or W == 1:
    print(1)
    exit()
    
if W % 2 == 0:
    ans = W // 2 * (math.ceil(H / 2) + math.floor(H / 2))
else:
    ans = W // 2 * (math.ceil(H / 2) + math.floor(H / 2)) + math.ceil(H / 2) 

print(ans)