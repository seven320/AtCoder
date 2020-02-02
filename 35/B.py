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

S = str(input())
T = int(input())

move = list(S)
cnt = 0
position = [0,0]
for i in range(len(move)):
    if move[i] == "?":
        cnt += 1
    elif move[i] == "L":
        position[0] += -1
    elif move[i] == "R":
        position[0] += 1
    elif move[i] == "U":
        position[1] += 1
    else:
        position[1] += -1
if T == 1:# max
    ans = abs(position[0]) + abs(position[1]) + cnt
else:
    if abs(position[0]) + abs(position[1]) - cnt >= 0:
        ans = abs(position[0]) + abs(position[1]) - cnt
    else:
        ans = (abs(position[0]) + abs(position[1]) - cnt) % 2
print(ans)
