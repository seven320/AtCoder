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
xy = [[] for i in range(N)]
for i in range(N):
    xy[i] = LI()

distances = []
def distance(town, town2):
    return ((town[0] - town2[0])**2 + (town[1] - town2[1])**2)**0.5

for i in range(N):
    for j in range(i+1,N):
        distances.append(distance(xy[i], xy[j]))

print(sum(distances) / N * 2)
