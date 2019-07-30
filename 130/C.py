# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

W,H,x,y = map(int,input().split())
area = W*H/2
if x == W/2 and y == H/2:
    cnt = 1
else:
    cnt = 0

print(area,cnt)
