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

N = int(input())
a = LI()

b = [0 for i in range(N)]
cnt = 0
for i in reversed(range(N)):
    part_sum = 0
    step_cnt = N // (i+1)
    for step in range(2,step_cnt+1):
        # print("step",step)
        part_sum += b[step * (i+1)-1]
    # print(part_sum)
    b[i] = (part_sum + a[i]) % 2

# print(b)
poss = []
for i in range(N):
    if b[i] == 1:
        cnt += 1
        poss.append(i+1)

print(cnt)
for pos in poss:
    print(pos)
