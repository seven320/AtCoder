# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import bisect
import numpy as np

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
s = []
for i in range(N):
    s.append(list(str(input())))

s_ = np.array(s)
s_rot = np.rot90(s_, 3)
for i in range(s_.shape[0]):
    for j in range(s_.shape[1]):
        print(s_rot[i,j],end="")
    print("")
